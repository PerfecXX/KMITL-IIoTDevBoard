from micropython import const
import framebuf

# Register definitions
SET_DISP = const(0xae)
SET_MEM_ADDR = const(0x20)
SET_DISP_START_LINE = const(0x40)
SET_SEG_REMAP = const(0xa0)
SET_MUX_RATIO = const(0xa8)
SET_COM_OUT_DIR = const(0xc0)
SET_DISP_OFFSET = const(0xd3)
SET_COM_PIN_CFG = const(0xda)
SET_DISP_CLK_DIV = const(0xd5)
SET_PRECHARGE = const(0xd9)
SET_VCOM_DESEL = const(0xdb)
SET_ENTIRE_ON = const(0xa4)
SET_NORM_INV = const(0xa6)
SET_CHARGE_PUMP = const(0x8d)
SET_COL_ADDR = const(0x21)
SET_PAGE_ADDR = const(0x22)
SET_CONTRAST = const(0x81)

class SSD1306:
    def __init__(self, width, height, external_vcc):
        self.width = width
        self.height = height
        self.external_vcc = external_vcc
        self.pages = self.height // 8
        self.buffer = bytearray(self.pages * self.width)
        self.framebuf = framebuf.FrameBuffer(self.buffer, self.width, self.height, framebuf.MONO_VLSB)

        # Graphics primitives
        self.fill = self.framebuf.fill
        self.pixel = self.framebuf.pixel
        self.hline = self.framebuf.hline
        self.vline = self.framebuf.vline
        self.line = self.framebuf.line
        self.rect = self.framebuf.rect
        self.fill_rect = self.framebuf.fill_rect
        self.text = self.framebuf.text
        self.scroll = self.framebuf.scroll
        self.blit = self.framebuf.blit

        self.poweron()
        self.init_display()

    def init_display(self):
        for cmd in (
            SET_DISP | 0x00,  # Display off
            SET_MEM_ADDR, 0x00,  # Horizontal addressing mode
            SET_DISP_START_LINE | 0x00,  # Start line at 0
            SET_SEG_REMAP | 0x01,  # Column address 127 mapped to SEG0
            SET_MUX_RATIO, self.height - 1,
            SET_COM_OUT_DIR | 0x08,  # Scan direction COM[N] to COM0
            SET_DISP_OFFSET, 0x00,
            SET_COM_PIN_CFG, 0x02 if self.height == 32 else 0x12,
            SET_DISP_CLK_DIV, 0x80,
            SET_PRECHARGE, 0x22 if self.external_vcc else 0xf1,
            SET_VCOM_DESEL, 0x30,  # 0.83 * Vcc
            SET_CONTRAST, 0xff,  # Maximum contrast
            SET_ENTIRE_ON,  # Output follows RAM content
            SET_NORM_INV,  # Not inverted
            SET_CHARGE_PUMP, 0x10 if self.external_vcc else 0x14,  # Charge pump
            SET_DISP | 0x01  # Display on
        ):
            self.write_cmd(cmd)
        self.fill(0)
        self.show()

    def poweroff(self):
        self.write_cmd(SET_DISP | 0x00)

    def poweron(self):
        self.write_cmd(SET_DISP | 0x01)

    def contrast(self, contrast):
        self.write_cmd(SET_CONTRAST)
        self.write_cmd(contrast)

    def invert(self, invert):
        self.write_cmd(SET_NORM_INV | (invert & 1))

    def rotate(self, rotate):
        self.write_cmd(SET_COM_OUT_DIR | ((rotate & 1) << 3))
        self.write_cmd(SET_SEG_REMAP | (rotate & 1))

    def show(self):
        x0 = 0
        x1 = self.width - 1
        if self.width == 64:  # 64-pixel wide displays are shifted by 32
            x0 += 32
            x1 += 32
        self.write_cmd(SET_COL_ADDR)
        self.write_cmd(x0)
        self.write_cmd(x1)
        self.write_cmd(SET_PAGE_ADDR)
        self.write_cmd(0)
        self.write_cmd(self.pages - 1)
        self.write_data(self.buffer)

    # Abstract methods for communication to be implemented in subclasses
    def write_cmd(self, cmd):
        raise NotImplementedError

    def write_data(self, buf):
        raise NotImplementedError

class SSD1306_I2C(SSD1306):
    def __init__(self, width, height, i2c, addr=0x3c, external_vcc=False):
        self.i2c = i2c
        self.addr = addr
        self.temp = bytearray(2)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.temp[0] = 0x80  # Co=1, D/C#=0
        self.temp[1] = cmd
        self.i2c.writeto(self.addr, self.temp)

    def write_data(self, buf):
        # Send data in chunks to avoid memory issues
        self.i2c.writeto_mem(self.addr, 0x40, buf)

class SSD1306_SPI(SSD1306):
    def __init__(self, width, height, spi, dc, res, cs, external_vcc=False):
        self.spi = spi
        self.dc = dc
        self.res = res
        self.cs = cs
        self.rate = 10 * 1024 * 1024
        dc.init(dc.OUT, value=0)
        res.init(res.OUT, value=0)
        cs.init(cs.OUT, value=1)
        super().__init__(width, height, external_vcc)

    def write_cmd(self, cmd):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs.high()
        self.dc.low()
        self.cs.low()
        self.spi.write(bytearray([cmd]))
        self.cs.high()

    def write_data(self, buf):
        self.spi.init(baudrate=self.rate, polarity=0, phase=0)
        self.cs.high()
        self.dc.high()
        self.cs.low()
        self.spi.write(buf)
        self.cs.high()
