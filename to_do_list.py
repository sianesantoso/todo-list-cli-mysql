import mysql.connector
from datetime import datetime 

db = mysql.connector.connect(
    host="localhost", user="root", password="", database="todolist"
)

cursor = db.cursor()

def main () :
    while True : 
        print('Menu : ')
        print('1. Lihat list')
        print('2. Tambah list')
        print('3. Update List')
        print('4. Delete List')
        print('5. Keluar')

        pilihanMenu = int(input('Maasukan pilihan input = '))

        if (pilihanMenu not in [1,2,3,4,5]) :
            print('input tidk valid')
            continue 

        if (pilihanMenu == 1) :
            cursor.execute("SELECT No, Nama_kegiatan, Waktu, Tempat FROM activity")
            data = cursor.fetchall()
            for x in data : 
                print(x)
        
        elif (pilihanMenu == 2) :
            namaKegiatan = input('Masukan nama kegiatan = ')
            tempatKegiatan= input('Masukan tempat kegiatan = ')
            waktuKegiatan = datetime.now()
            waktuKegiatan = waktuKegiatan.strftime("%H:%M:%S")
            print(waktuKegiatan)
            query1 = "INSERT INTO activity (Nama_kegiatan, Waktu, Tempat) VALUES (%s, %s, %s)"
            value1 = (namaKegiatan,waktuKegiatan,tempatKegiatan)

            cursor.execute(query1,value1)
            db.commit()

        elif (pilihanMenu == 3) :
            idInput = int(input('Masukan no = ')) 

            namaKegiatan = input('Masukan nama kegiatan = ')
            tempatKegiatan= input('Masukan tempat kegiatan = ')
            waktuKegiatan = datetime.now()
            waktuKegiatan = waktuKegiatan.strftime("%H:%M:%S")

            query2 = f"UPDATE activity set Nama_kegiatan = '{namaKegiatan}', Waktu = '{waktuKegiatan}', Tempat = '{tempatKegiatan}' WHERE No = '{idInput}'"
            cursor.execute(query2)
            db.commit()

        elif (pilihanMenu == 4) :
            idInput = int(input('Masukan no = ')) 
            query3 = f"DELETE FROM activity WHERE No = '{idInput}'"
            cursor.execute(query3)
            db.commit()

        else : 
            break 

main()