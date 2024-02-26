import mysql.connector
def ADD():
    ''' To add a customer to the customer table'''
    mycon = mysql.connector.connect(host='localhost', database= 'ride_bookings')
    mycursor = mycon.cursor(buffered=True)

    sql = 'Select c_id from customer order by length(c_id),c_id'
    mycursor.execute(sql)
    cgen = mycursor.fetchall()
    if mycursor.rowcount:
        cgen = int(cgen[-1][0][1:])
        c_id = 'C' + str(cgen +1)
    else:
        c_id = 'C1'

    name = input('Enter your name: ').upper()
    while True:
        try:
            mob1 = int(input('Enter cell phone number: '))
            if len(str(mob1)) !=8:
                print("Error, cell phone number should only have 8 digits.")
                continue
            sql = 'Select * from customer where mobile_1 = %d' % mob1
            mycursor.execute(sql)
            if mycursor.rowcount:
                print('This cell phone number already exists, please try again.')
                continue
        except:
            print('Invalid cell phone number entered. Please try again.')
            continue
        break
    while True:
        email = input('Enter email address: ').lower()
        sql = "select * from cusotmer where email='%s" % email
        mycursor.execute(sql)
        mycursor.fetchall()
        if mycursor.rowcount:
            print('This email address alreayd exisits, please try again.')
            continue
        break
    address = input('Please enter your address: ').upper()

    data = (c_id, name, mob1, email, address, 0, 'I')
    sql = 'insert into customer values ('%s', '%s', %d, '%s', '%s', %d, '%s')' % data

    mycursor.execute(sql)
    mycon.commit()
    mycon.close()

    print('\nCustomer has been successfully added')
    print("Your Customer ID is ", c_id)

    return c_id