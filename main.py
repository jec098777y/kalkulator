#1: 0x00FF30CF
#2: 0x00FF18E7
#+: 0x00FFA857
#-: 0x00FFE01F
#=: 0x00FF906F
OLED.init(128, 64)
pierwsza_cyfra = ""
druga_cyfra = ""
co_robic = ""
wynik = 0
makerbit.connect_ir_receiver(DigitalPin.P8, IrProtocol.NEC)
def on_ir_datagram():
    global pierwsza_cyfra
    global druga_cyfra
    global co_robic
    global wynik
    
    kod = makerbit.ir_datagram()
    
    if kod == "0x00FF30CF":
        if co_robic != "":
            druga_cyfra += "1"
        else:
            pierwsza_cyfra += "1"
       
        
    elif kod == "0x00FF18E7":
    
        if co_robic != "":
            druga_cyfra += "2"
        else:
            pierwsza_cyfra += "2"

        pass
    
    if kod == "0x00FFA857":
        co_robic = "+"
        pass
    if kod == "0x00FFE01F":
        co_robic = "-"
        
    OLED.clear()
    OLED.write_string_new_line(":" + pierwsza_cyfra + co_robic + druga_cyfra)
    
    if kod == "0x00FF906F":
        if co_robic == "+":
            wynik = int(pierwsza_cyfra) + int(druga_cyfra)
      
            OLED.write_num_new_line(wynik)
        else:
            wynik = int(pierwsza_cyfra) - int(druga_cyfra)
            OLED.write_num_new_line(wynik)
        pierwsza_cyfra = ""
        druga_cyfra = ""
        co_robic = ""
            
makerbit.on_ir_datagram(on_ir_datagram)