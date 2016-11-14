# turning-clicker
Turning Technologies clicker emulation for the Arduino

The included sketch emulates the Turning Technologies clicker base station, to be used with the Turning Technologies ResponseCard RF (including ResponseCard RF LCD, though I'm not sure what other kinds exist). Its current behavior is to acknowledge all clicker "responses" (i.e. cause the LCD to blink green) and then send the address/data to a computer via Serial. The format is quite verbose, and the code could easily be extended to use a more structured approach like Firmata. Example output from boot is as follows:

    *** booting ***
    STATUS     = 0x0e RX_DR=0 TX_DS=0 MAX_RT=0 RX_P_NO=7 TX_FULL=0
    RX_ADDR_P0-1   = 0xd30f09 0x123456
    RX_ADDR_P2-5   = 0xc3 0xc4 0xc5 0xc6
    TX_ADDR    = 0xd30f09
    RX_PW_P0-6   = 0x06 0x06 0x00 0x00 0x00 0x00
    EN_AA    = 0x00
    EN_RXADDR  = 0x02
    RF_CH    = 0x29
    RF_SETUP   = 0x05
    CONFIG     = 0x07
    DYNPD/FEATURE  = 0x00 0x00
    Data Rate  = 1MBPS
    Model    = nRF24L01+
    CRC Length   = Disabled
    PA Power   = PA_HIGH


    incoming: 090fd331ee8c --> 1
    outgoing: 090fd3067b34
    incoming: 090fd332deef --> 2
    outgoing: 090fd3067b34
    incoming: 090fd333cece --> 3
    outgoing: 090fd3067b34
    incoming: 090fd334be29 --> 4
    outgoing: 090fd3067b34
    incoming: 090fd335ae08 --> 5
    outgoing: 090fd3067b34
    incoming: 090fd3369e6b --> 6
    outgoing: 090fd3067b34
    incoming: 090fd33f0f42 --> ?
    outgoing: 090fd3067b34

## Motivation

I created this because there didn't seem to be any "clean" solutions to clicker emulation online. This is partially based off the work of [Taylor Killian](http://www.taylorkillian.com/2012/11/turning-point-clicker-emulation-with.html) and [Travis Goodspeed](https://travisgoodspeed.blogspot.com/2010/07/reversing-rf-clicker.html). Their posts were incredibly helpful in getting everything set up. Also incredibly helpful was the [Arduino-info wiki](https://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo) with all their general nRF24L01 information.

## Hardware

The hardware used in this project was an Arduino Nano clone, a nRF24L01+ breakout board, and an accompanying base module / voltage regulator as pictures on the [Arduino-info wiki](https://arduino-info.wikispaces.com/Nrf24L01-2.4GHz-HowTo). They were all generic devices from eBay, anything similar should work.

## Library dependencies

* [The TMRh20 RF24 library](https://github.com/TMRh20/RF24)
* [FastCRC](https://github.com/FrankBoesing/FastCRC)

## Contact

nmooney@cs.washington.edu
