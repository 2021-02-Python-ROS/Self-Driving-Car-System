#!/usr/bin/env python

class ScanWithCamera:
    # Scan With Camera - Bot Behavior Change
    def __init__(self, scan_method):
        self.scan_method = scan_method
        
    def set_bot_behavior(self, scan_method):
        self.scan_method = scan_method
    
    def do_behavior(self):
        self.scan_method.do_behavior()
