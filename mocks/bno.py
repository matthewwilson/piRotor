class BNO:

    def begin(self):
        print("Checking if BNO is ready")
        return True

    def get_system_status(self):
        return 5, 0x0f, 0x00

    def get_revision(self):
        return 776, 21, 0xFB, 0x32, 0x0f

    def read_euler(self):
        return 0.0, 0.0, 0.0
