import spacy

nlp=spacy.load("output/models/model-best")

address_list=["130 W BOSE ST STE 100, PARK RIDGE, IL, 60068, USA",
              "en description Postage on Account GB International Priority Royal Mail Privacy policy www royalmail com privacy AIR MAIL PAR AVION 08 011 721 2000 030 227 184 UY 7932 5657 0GB Kimberley Kubath 112 George St 1102 Toronto Ontario M5A 2M5 CANADA Customer Reference 701 4511620 6554647 Department reference 1783881944561 Retun Address 1 Apollo Rise GU14 0GT",
              "8311 MCDONALD RD, HOUSTON, TX, 77053-4821, USA",
              "PO Box 317, 4100 Hwy 20 E Ste 403, NICEVILLE, FL, 32578-5037, USA",
              "C/O Elon Musk Innovations Inc, 1548 E Florida Avenue, Suite 209, TAMPA, FL, 33613, USA",
              "Seven Edgeway Plaza, C/O Mac Dermott Inc, OAKBROOK TERRACE, IL, 60181, USA",
               "en description 135 EF lizeriz 304 261u 304 261 YYZ1 4  DT03 Geraldine Mercado 11 Street SUITE S533 M5A 2M5 Toronto Ontario Canada TBC369899292009 CYCLE 1 YYZ4 O T03 YHM5 C ART ",
               "en description YYZ1 1 6 Lbs 02 06 DT03 Alison Roy 1503 112 George Street M5A 2M5 Toronto Ontario Canada Not restricted as per special provision A199 TBC370081708009 DT03 CYCLE 1 YYZ7 O T03 YHM5 C ART livr Is MhmbHHtj ",
               "en description GIES in M7vxB3 1 404 based Dia riqu 303 251e 303 240 par e v 303 251g 303 251tale orn size 6 n 303 251 talle 6 Ou Sont mounl 303 251es simplement avec une d al humedecerse Si observa una peque 303 261a on una toallita para beb 303 251s o un pa 303 261o h 303 272medo un keep plastic bags away from babies a to their mouths To avoid risk of choking e most articles of clothing HUGGIES 302 256 dia INGE8XAL 1 404 IMPORTANT Pour 303 251viter tout risque de ATTENTION Les enfants peu un b 303 251b 303 251 d 303 251chirer lac risquent de of flame 22 YYZ1 5 5 Lbs 02 06 DT03 Nell Chitty N711 116 George St M5A 3S2 Toronto Ontarlo Canada TBC369722990009 DT03 CYCLE YYZ2 Y HM5 YHM5 D T03 ",
               "en description apide delivery fast free livraiso YYZ1 3  02 06 DT03 John Michael Tamburro S430 112 George Street M5A 2M5 Toronto Ontario Canada TBC369836993009 DT03 CYCLE 1 YYZ9 T03 MajrWHwSj 3 106 MajrWHwSj 3 106" ,
               "en description A 18 3C YCLE 1 livrais et gr RIB 6424 IBC369753115009 DTOS 02 06 YYZ1 0 6 Lbs Dave Creamer S518 112 George Street M5A 2M5 Toronto Ontario Canada TBC369753115009 CYCLE 1 DT03 YYZ4 O T03 YHM5 C ART 1 3031", 
               "en description MtWq3NZOj UVles tv streamina YYZ1 1 2 Lbs 02 06 DT03 Antoine Lebrun N1404 116 George Street M5A 3S2 Toronto Ontario Canada TBC370042221009 CYCLE 1 DT03 YYZ9 T03 series ",
               "en description YYZ1 1  02 06 DT03 Nell Chitty 116 George Street Unit 711 M5A 3S2 Toronto Ontario Canada Not restricted as per special provision A123 TBC369659309009 DT03 CYCLE 1 YYZ9 T03 MtmJs 7C4j 4 105 MimJs7C4j 41 105 "
               "en description REAKBULK entiro Sy stems v 1 1 16 1605 BBX HL Contact FROM Mango Barcelona Origin Mercaders 9 11 Pol Ind Riera de Caldes 08184 Palau Solit Plegamans SPAIN BCN TO leah travaglini 2008 112 george street Contact 4169995948 M5A 2M5 TORONTO Canada CA YHM YTZ Day Time Ret code Pickup date Package Shpt Wght Piece CYD08J00 0 20kg 0 20kg 1 1 2022 02 01 Content Clothes Cleared under waybill WAYBILL 98 4285 7765 2L 303 207AM5A2M5 41000000 00 38427907 500553542 9 SAP 3001 101 PED 00 38427907500553542 Canada leah travaglini 01 02 22 T Clent sig nature CYD08J00" ]

# Checking predictions for the NER model
for address in address_list:
    doc=nlp(address)
    ent_list=[(ent.text, ent.label_) for ent in doc.ents]
    print("Address string -> "+address)
    print("Parsed address -> "+str(ent_list))
    print("******")



address="C/o John Doe LLC, 111 8th Avenue Ste 1301, Tulsa, Oklahoma, 74136–1922, USA"
doc=nlp(address)
ent_list=[(ent.text, ent.label_) for ent in doc.ents]
print("Address string -> "+address)
print("Parsed address -> "+str(ent_list))

# Loading Entity Ruler coupled NER model and checking prediction
nlp=spacy.load("output/models/model-best")

doc=nlp(address)
ent_list=[(ent.text, ent.label_) for ent in doc.ents]
print("Address string -> "+address)
print("Parsed address -> "+str(ent_list))