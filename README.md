# RemoteConnectionWrapper
A Python Wrapper for the RemoteConnection SCP:SL EXILED plugin

This wrapper requires [this plugin](https://github.com/HelpMeGame/SCPSLRemoteConnection) to be installed and configured on the SCP:SL Server.

## How to use
Python 3 is required for this wrapper.

### Discord Bot
The Discord Bot requires `discord.py` and `python-dotenv` which can both be installed through `pip`.
1. Download and Extract the files from the Release Tab.
2. Create a file named `.env`, and add `TOKEN = <your bot token>`.
3. Open `commands.py` and on line 10, change the `IP`, `Port`, and `Password` to the correct values.
4. Start your SCP:SL server, and run the `bot.py` file to start the bot. 
The default prefix for the bot is `=`.

####Discord Bot Commmands
- `playerlist`/`pl` - Displays Player List
- `uptime` - Displays Uptime
*(The following commands require a role with Admin to use.)*
- `broadcast <message>` - Broadcast a message to the SCP:SL server
- `ban <player game ID>` - Bans a player for a month
- `kick <player game ID>` - Kicks a player


### Creating a server socket
A Server socket can be created by calling `serverhandler.SCPSL(ip, port, password)`. This will create an object of the SCPSL class, that contains basic commands and actions for the plugin.

The following are functions that you can run from the `SCPSL` class.
- `.get_player_list()` returns a list of players, thier Unique ID, and thier Game ID.
- `.get_uptime()` - Returns the number of minutes the server has been running for.
- `.broadcast()` - Broadcasts a message to the server for 5 seconds.
- `.ban_player()` - Bans a Player using their Game ID.
- `.kick_player()` - Kicks a Player using their Game ID.

### Sending Information
The wrapper uses a function (`.connect_to_socket()`) to connect to the Server, and pass/recieve information. This info is then used server side, and a response and handed back. The sockets then disconnect, allowing for future use in the same port. In this wrapper, when a command is passed through `.connect_to_socket()`, a class named `CommandJson` is created, containing the information that needs to be sent. It is converted to JSON, then passed to the server. The response from the server is parsed back into a seperate class named `ReturnJson` which contains the `command_type` passed through, the `result`, and `success` (which will either be `1` or `0`.)


For mote information on how the JSON should be formatted, check the [main plugin repo](https://github.com/HelpMeGame/SCPSLRemoteConnection).
