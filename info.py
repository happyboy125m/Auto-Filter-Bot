# info.py
# ─────────────────────────────────────────────────────────────
# Stores and manages all informational messages and links
# for the Telegram Movie Bot (welcome, about, support, etc.)
# ─────────────────────────────────────────────────────────────

import datetime
import platform
import psutil


class BotInfo:
    """
    BotInfo manages all bot-related messages, system info,
    and general settings like channels, groups, and developer info.
    """

    def __init__(self):
        # ─────────────── Basic Bot Info ───────────────
        self.bot_name = "🎬 Movie Finder Bot"
        self.version = "2.1.0"
        self.developer = "@YourUsername"
        self.created_on = "November 2025"

        # ─────────────── Bot Links ───────────────
        self.request_channel = "https://t.me/YourRequestChannel"
        self.request_group = "https://t.me/YourRequestGroup"
        self.support_channel = "https://t.me/YourSupportChannel"
        self.update_channel = "https://t.me/YourUpdatesChannel"
        self.repo_link = "https://github.com/yourusername/movie-finder-bot"
        self.demo_bot = "https://t.me/YourBotUsername"

        # Track uptime
        self.start_time = datetime.datetime.now()

    # ───────────────────────────────────────────────
    # WELCOME MESSAGE (for /start command)
    # ───────────────────────────────────────────────
    def get_welcome_message(self, user_first_name: str) -> str:
        return f"""
👋 **Welcome {user_first_name}!**

🎥 *{self.bot_name}* helps you find movies instantly — with details, ratings, and download/request options.

✨ **Features:**
• Search movies by name 🎬  
• Get IMDb ratings ⭐  
• Request missing movies 📩  
• Get latest updates 🔔  

📢 **Join our community:**
- Request Channel: [Click Here]({self.request_channel})
- Request Group: [Join Here]({self.request_group})
- Updates: [Follow Here]({self.update_channel})

💡 Type `/help` to see available commands.

_— Developed by {self.developer}_
"""

    # ───────────────────────────────────────────────
    # ABOUT MESSAGE (/about command)
    # ───────────────────────────────────────────────
    def get_about_message(self) -> str:
        return f"""
🤖 **About {self.bot_name}**

📦 *Version:* {self.version}  
👨‍💻 *Developer:* {self.developer}  
🗓️ *Created On:* {self.created_on}  
🔗 *Repository:* [GitHub Link]({self.repo_link})  
🤖 *Demo Bot:* [Try Here]({self.demo_bot})

💬 *Support Channel:* [Join Here]({self.support_channel})
📢 *Updates:* [Follow Here]({self.update_channel})
"""

    # ───────────────────────────────────────────────
    # HELP MESSAGE (/help command)
    # ───────────────────────────────────────────────
    def get_help_message(self) -> str:
        return """
🧭 **Bot Commands:**

`/start` — Start the bot and get welcome message  
`/help` — Show this help message  
`/about` — Get bot info and developer details  
`/request <movie name>` — Request a movie  
`/top` — Show top-rated movies  
`/info` — Show system and uptime info

💡 Tip: Type the movie name directly to search it.
"""

    # ───────────────────────────────────────────────
    # SYSTEM INFO (/info command)
    # ───────────────────────────────────────────────
    def get_system_info(self) -> str:
        try:
            uptime = datetime.datetime.now() - self.start_time
            cpu = psutil.cpu_percent()
            ram = psutil.virtual_memory().percent
            sys_info = platform.platform()

            return f"""
🧠 **System Information:**

⏱️ *Uptime:* {uptime.days}d {uptime.seconds // 3600}h {(uptime.seconds % 3600) // 60}m  
💻 *System:* {sys_info}  
⚙️ *CPU Usage:* {cpu}%  
💾 *RAM Usage:* {ram}%  
"""
        except Exception as e:
            return f"❌ Failed to get system info: {e}"

    # ───────────────────────────────────────────────
    # For debugging (if run directly)
    # ───────────────────────────────────────────────
    def display_all(self):
        print(self.get_about_message())
        print(self.get_system_info())


# ───────────────────────────────────────────────
# Example usage (run directly to test)
# ───────────────────────────────────────────────
if __name__ == "__main__":
    info = BotInfo()
    print(info.get_welcome_message("Happy"))
    print(info.get_about_message())
    print(info.get_help_message())
    print(info.get_system_info())
