from evennia import DefaultScript, TICKER_HANDLER
from evennia.utils import time_format
from evennia.contrib.rpg.buffs import BuffHandler
import time

class PlayerBuffsManager(DefaultScript):
    """
    Script to manage and track player buffs, stats, and variables in real-time.

    Tracks:
    - Health, Mana, Stamina
    - Buffs/Debuffs (using BuffHandler)
    - Durations and timers
    - Sated levels (e.g., hunger/thirst)
    - Age, Time played
    - Currencies
    """
    def at_script_creation(self):
        """
        Called when the script is first created.
        """
        self.key = "player_buffs_manager"
        self.desc = "Tracks and manages player buffs, stats, and variables."
        self.persistent = True  # Survives server reloads

        # Initialize tracked attributes
        self.db.stats = {
            "health": 100, "max_health": 100,
            "mana": 100, "max_mana": 100,
            "stamina": 100, "max_stamina": 100,
            "sated_level": 100,  # Hunger/Thirst
            "age": 0,
            "time_played": 0,
            "currencies": {"gold": 0, "silver": 0, "copper": 0},
        }

        # BuffHandler initialization
        if not hasattr(self.obj, "buffs"):
            self.obj.buffs = BuffHandler(self.obj)

        # Start periodic updates
        self.start_updates()

    def start_updates(self):
        """
        Starts ticker updates for real-time tracking.
        """
        # Update stats every 60 seconds
        TICKER_HANDLER.add(60, self.update_time_played, id(self))

    def stop_updates(self):
        """
        Stops ticker updates.
        """
        TICKER_HANDLER.remove(60, self.update_time_played, id(self))

    def update_time_played(self):
        """
        Updates player's time played and age.
        """
        stats = self.db.stats
        stats["time_played"] += 60  # Increment time played by 1 minute
        stats["age"] = stats["time_played"] // 3600  # Convert to hours
        self.obj.db.time_played = stats["time_played"]
        self.obj.db.age = stats["age"]

        self.obj.msg(f"|wTime Played|n: {time_format(stats['time_played'])}, |wAge|n: {stats['age']} hours.")

    def apply_buff(self, buff_name, duration, **effects):
        """
        Apply a buff or debuff to the player.

        Args:
            buff_name (str): Name of the buff.
            duration (int): Duration in seconds.
            effects (dict): Stat modifications, e.g., {"health": +10}.
        """
        self.obj.buffs.add(buff_name, duration, **effects)
        self.obj.msg(f"|g{buff_name} applied for {duration} seconds.|n")

    def at_repeat(self):
        """
        Called periodically by the script for real-time tracking.
        """
        stats = self.db.stats

        # Update hunger/thirst
        stats["sated_level"] = max(stats["sated_level"] - 1, 0)
        if stats["sated_level"] == 0:
            self.obj.msg("|rYou feel famished and weak.|n")

        # Apply over-time effects from BuffHandler
        for buff in self.obj.buffs.get_all():
            for stat, value in buff["effects"].items():
                stats[stat] = min(stats[stat] + value, stats[f"max_{stat}"])

        # Save the updated stats back
        self.db.stats = stats
        self.obj.db.stats = stats

    def at_script_delete(self):
        """
        Clean up when script is deleted.
        """
        self.stop_updates()

# Self-loading script
def at_server_start():
    """
    Hook to ensure the script attaches itself to all characters on server start.
    """
    from evennia import search_script_tag
    from evennia.utils.search import search_object

    # Attach script to all characters
    for char in search_object(tag="player", typeclass="typeclasses.characters.Character"):
        if not char.scripts.get("player_buffs_manager"):
            char.scripts.add(PlayerBuffsManager)
