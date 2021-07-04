import socket
import json

HOST = '127.0.0.1'
PORT = 886


class CommandJson:
    def __init__(self, command, args: list, password):
        self.command = command
        self.args = args
        self.password = password


class ReturnJson:
    def __init__(self, command_type, result, success):
        self.command_type = command_type
        self.result = result
        self.success = success


class SCPSL:
    def __init__(self, ip, port, password):
        self.ip = ip
        self.port = port
        self.password = password

    def get_player_list(self):
        playerlist = self.connect_to_socket("playerlist")
        return playerlist.result

    def get_uptime(self):
        uptime = self.connect_to_socket("uptime")
        return uptime.result

    def broadcast(self, message):
        broadcast = self.connect_to_socket("broadcast", [message])
        return broadcast.result

    def ban_player(self, players: []):

        success, players = check_for_number(players)
        if not success:
            return

        result = self.connect_to_socket("ban", players)
        return result.result

    def kick_player(self, players: []):

        success, players = check_for_number(players)
        if not success:
            return

        result = self.connect_to_socket("kick", players)
        return result.result

    def connect_to_socket(self, command: str, args: list = []):
        to_send = json.dumps(CommandJson(command, args, self.password).__dict__)

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((self.ip, self.port))
            s.sendall(bytes(to_send, 'utf-8'))
            data = s.recv(1024)
            s.close()

        returned = json.loads(data.decode('utf-8'))
        returned = ReturnJson(returned['commandType'], returned['result'], returned['success'])

        return returned


def check_for_number(to_check: []):
    for x in range(0, len(to_check)):
        try:
            int(to_check[x])
            to_check[x] = str(to_check[x])
        except:
            return 0, None
    return 1, to_check
