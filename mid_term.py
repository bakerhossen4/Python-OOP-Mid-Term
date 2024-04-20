class Star_Cinema :
    hall_list = []
    def entry_hall ( self, hall_ob ) :
        #hall = Hall( self.rows, self.cols, self.hall_no )
        self.hall_list.append( hall_ob )
        
class Hall(Star_Cinema):
    def __init__(self, rows, cols, hall_no ):
        self.rows = rows
        self.cols = cols
        self.hall_no = hall_no
        self.seats = {}
        self.show_list = []
        stcinema = Star_Cinema()
        stcinema.entry_hall(self)

    def entry_show( self, id, movie_name, time ) :
        a = ( id, movie_name, time )
        self.show_list.append( a )
        seatList = [
                    [0 for _ in range(self.rows)] for _ in range(self.cols) 
                    ]  
        self.seats[id] = seatList

    def view_show_list( self ) :
        for i in self.show_list :
            print( 'Movie :', end = '')
            for j in i :
                print( ' ', j, end = '', sep = ' ' )
            print()

    def view_availale_seats( self ) :
        user = int(input('Enter Show Id : ' ))
        if user in self.seats :
            print(self.seats[user])
        else :
            print('Wrong ID of Show ')

    def book_seats( self ) :
        use = int(input('Show ID : '))
        t = int(input('Number of Ticket(Pls Give 1 as input) : '))
        m = int(input('Enter Row : '))
        n = int(input('Enter Col : '))
        if m > 10 or n > 10 :
            print( 'Invalid Seat Booking request...(10 * 10 matrix ) Give the correct input. ' )
        elif self.seats[use][m - 1][n - 1] == 0 :
            self.seats[use][m - 1][n - 1] = 1
        else :
            print('Already Booked. Please Try Another Seats.....')
        print(self.seats[use])

    def __repr__(self) -> str:
        return f'{self.rows}, {self.cols}, {self.hall_no}'

hall1 = Hall( 10, 10, 1 )
print( hall1.hall_list )
hall1.entry_show( 111, 'Jumanji', '19/04/24' )
hall1.entry_show( 222, 'Spiderman', '19/04/24' )
while True :
    print('-----------------------')
    print('1. View All Show Today ')
    print('2. View Available Seats ')
    print('3. Book Tickets ')
    print('4. Exit ')
    print('-----------------------')
    user = int(input('Enter Option : '))
    if user == 1 :
        hall1.view_show_list()
    elif user == 2 :
        hall1.view_availale_seats()
    elif user == 3 :
        hall1.book_seats()
    elif user == 4 :
        break
    