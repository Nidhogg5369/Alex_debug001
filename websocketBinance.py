import threading
import websocket
import gzip
import ssl
import logging
from urllib import parse
import urllib.parse

import gzip
import json
import asyncio

class webSocketBinance:
    def __init__(self, url):
        self.isOpened = False
        self._url = url

        self._ws = websocket.WebSocketApp(url,
                                          on_open=self._on_open,
                                          on_message=self._on_message,
                                          on_close=self._on_close,
                                          on_error=self._on_error)

    def _on_open(self, ws):
        print('连接成功.')

    def _on_message(self, ws, msgBinary):
        print(f"收到：{msgBinary}")

    def _on_error(self, ws, error):
        print(error)

    def _on_close(self, ws, close_status_code, close_msg):
        print(f"### closed ###\n {close_msg}")
        self._ws.run_forever()

    async def disconnect(self):
        self._ws.close()
        print("000")

    def start(self):
        self._ws.run_forever()


if __name__ == "__main__":
    #websocket.enableTrace(True) wss://fstream.binance.com/stream?streams=btcusdt@depth5@100ms/btcusdt@trade
    aa = webSocketBinance('wss://fstream.binance.com/stream?streams=btcusdt@depth5@100ms/btcusdt@trade')
    aa.start()
    asyncio.get_event_loop().run_forever()