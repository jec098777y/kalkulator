// 1: 0x00FF30CF
// 2: 0x00FF18E7
// +: 0x00FFA857
// -: 0x00FFE01F
// =: 0x00FF906F
OLED.init(128, 64)
let pierwsza_cyfra = ""
let druga_cyfra = ""
let co_robic = ""
let wynik = ""
makerbit.connectIrReceiver(DigitalPin.P8, IrProtocol.NEC)
makerbit.onIrDatagram(function on_ir_datagram() {
    
    
    
    
    let kod = makerbit.irDatagram()
    if (kod == "0x00FF30CF") {
        if (co_robic != "") {
            druga_cyfra += "1"
        } else {
            pierwsza_cyfra += "1"
        }
        
    } else if (kod == "0x00FF18E7") {
        if (co_robic != "") {
            druga_cyfra += "2"
        } else {
            pierwsza_cyfra += "2"
        }
        
        
    }
    
    if (kod == "0x00FFA857") {
        co_robic = "+"
        
    }
    
    if (kod == "0x00FFE01F") {
        co_robic = "-"
    }
    
    if (kod == "0x00FF906F") {
        if (co_robic == "+") {
            wynik = "=" + ("" + (parseInt(pierwsza_cyfra) + parseInt(druga_cyfra)))
        } else {
            wynik = "=" + ("" + (parseInt(pierwsza_cyfra) - parseInt(druga_cyfra)))
        }
        
        pierwsza_cyfra = ""
        druga_cyfra = ""
        co_robic = ""
        wynik = ""
    }
    
    OLED.writeString(pierwsza_cyfra + co_robic + druga_cyfra + wynik)
})
