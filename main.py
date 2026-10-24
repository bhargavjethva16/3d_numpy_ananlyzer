
import numpy as np




class data_analytics :
    
    def __init__(self):
        
        self.arr = None
        pass
    

    
    def create_numpy(self):
       
        
        print()
        print("Select the type of Array to create: ")
        print()
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        print()

        choice = int(input("Enter choice:-  "))
        print()

        if choice == 1 :
           
            elem = input("Enter the Elements for 1D Array (separated by space):-  ").split(",")
            elem = list(map(int,elem))
            arr = np.array(elem)
            self.arr = arr
            print("Array created successfully:")
        
            print(arr)
            print()
            return arr

        elif choice == 2 :
            
            row = int(input("Enter the No. for Row(s):-  "))
            cols = int(input("Enter the No. for Column(s):-  "))
            elem = input(f"Enter {row*cols} elements for the Array separated by space [2D Array] :-  ").split()
            elem = list(map(int,elem))
            arr = np.array(elem).reshape((row,cols))
            self.arr = arr
            print()
            print("Array created successfully:")
            print(arr)
            print()
            return arr

        elif choice == 3 :

            layer = int(input("Enter the No. for Layer(s):-  "))
            row = int(input("Enter the No. for Row(s):-  "))
            cols = int(input("Enter the No. for Column(s):-  "))

            elem = input(f"Enter {layer*row*cols} elements for the Array separated by space [3D Array] :-  ").split()
            elem = list(map(int,elem))
            arr = np.array(elem).reshape((layer,row,cols))
            self.arr = arr
            print()
            print("Array created successfully:")
            print(arr)
            print()
            return arr
        
        else:
            print("Invalid choice")
            return None

    def index_slice(self,main_arr):

        while True : 

            print()
            print("Choose an option:")
            print()
            print("1. Indexing")
            print("2. Slicing")
            print("3. Go back to Main Menu")
            print()

            ch = int(input("Enter your choice:  "))
            print()

            if ch == 1:
                    if main_arr.ndim == 1 :
                        
                        ind=int(input("Enter a Index number:  "))
                        print("Indexed Array:")
                        
                        print(main_arr[ind])
                        print()
                    
                    elif main_arr.ndim == 2 :
                        
                        ind=int(input("Enter a Row number:  "))
                        ind2=int(input("Enter a Column number:  "))
                        print("Indexed Array:")
                        print(main_arr[ind,ind2])
                        print()
                    
                    elif main_arr.ndim == 3 :
                        
                        dep=int(input("Enter Layer number:  "))
                        ind=int(input("Enter a Row number:  "))
                        ind2=int(input("Enter a Column number:  "))
                        print("Indexed Array:")
                        print(main_arr[dep,ind,ind2]) 
                        print()
            elif ch==2:
                    if main_arr.ndim == 1:
                        
                        row_range=input("Enter the Index Range (start:end) : ")
                        r_start, r_end = map(int, row_range.split(":"))
                        print("Sliced Array: ")
                        print(main_arr[r_start:r_end])

                    elif main_arr.ndim == 2:
                        
                        row_range=input("Enter the Row Range (start:end) : ")
                        col_range=input("Enter the Column Range (start:end) : ")
                        r_start,r_end = map(int, row_range.split(":"))
                        c_start,c_end = map(int, col_range.split(":"))
                        print("Sliced Array: ")
                        print(main_arr[r_start:r_end,c_start:c_end])
                        print()

                    elif main_arr.ndim == 3:
                        
                        layer_range=input("Enter the Layer Range (start:end):  ")
                        row_range=input("Enter the Row Range (start:end):  ")
                        col_range=input("Enter the Column Range (start:end):  ")
                        l_start, l_end = map(int, layer_range.split(":"))
                        r_start, r_end = map(int, row_range.split(":"))
                        c_start, c_end = map(int, col_range.split(":"))
                        print("Sliced Array: ")
                        print(main_arr[l_start:l_end,r_start:r_end,c_start:c_end])
                        print()

            elif ch == 3 : 
                print()
                print("Going back to Main Menu")
                print()
                break

            else:
                print("Invalid choice")


    def math_op(self,main_arr):

        print()
        print("="*32)
        print("Choose a Mathematical Operation:")
        print("="*32)
        print()
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print()

        
        opt = int(input("Enter No. betweeen 1 to 4:-  ")) 
        
        if opt == 1 :
           
            same = input(f"Enter the same size array Elements ({main_arr.size} elements separated by space) :  ").split()
            second_arr = list(map(int,same))

            if len(second_arr) != main_arr.size:
                print(f"Please enter exactly {main_arr.size} elements.")
                return

            second_arr = np.array(second_arr).reshape(main_arr.shape)
            print()

            print("Original Array : ")
            print(main_arr)
            print()
            print("Second Array :")
            print(second_arr)
            print()
            print("Result of Addition : ")
            print(main_arr + second_arr)

        elif opt == 2 : 
            
            same_size= input(f"Enter the same size elements ({main_arr.size} elements separated by space) : ").split()
            sec_arr = list(map(int,same_size))

            if len(sec_arr) != main_arr.size:
                print(f"Please enter exactly {main_arr.size} elements.")
                return

            sec_arr = np.array(sec_arr).reshape(main_arr.shape)
            print()

            print("Original Array : ")
            print(main_arr)
            print()
            print("Second Array : ")
            print(sec_arr)
            print()
            print("Result of Subtraction")
            print(main_arr-sec_arr)
            print()


        elif opt == 3 :
            same  = input(f"Enter the same size elements ({main_arr.size} elements separated by space) :  ").split()
            seco_arr = list(map(int,same))

            if len(seco_arr) != main_arr.size:
                print(f"Please enter exactly {main_arr.size} elements.")
                return

            seco_arr = np.array(seco_arr).reshape(main_arr.shape)
            print()

            print("Original Array : ")
            print(main_arr)
            print()
            print("Second Array : ")
            print(seco_arr)
            print()
            print("Result of Multiplication")
            print(main_arr*seco_arr)

        elif opt == 4 : 
             
             same  = input(f"Enter the same size elements ({main_arr.size} elements separated by space) :  ").split()
             seco_arr = list(map(int,same))

             if len(seco_arr) != main_arr.size:
                 print(f"Please enter exactly {main_arr.size} elements.")
                 return

             seco_arr = np.array(seco_arr).reshape(main_arr.shape)
             print()

             print("Original Array : ")
             print(main_arr)
             print()
             print("Second Array : ")
             print(seco_arr)
             print()

             if np.any(seco_arr == 0):
                 print("Division by zero is not allowed.")
                 return

             print("Result of Division:")
             print(main_arr/seco_arr)

        else:
            print("Invalid choice")


    def combine_arr(self,main_arr):
        try:
            print()
            print("Choose an option:")
            print()
            print("1. Combine Array")
            print("2. Split Array")
            print()

            cho = int(input("Enter your choice:  "))

            if cho == 1 :

                bok = input(f"Enter the elements of another Array to combine ({main_arr.size} elements separated by space) :  ").split()
                spi_arr = list(map(int,bok))

                if len(spi_arr) != main_arr.size:
                    print(f"Please enter exactly {main_arr.size} elements.")
                    return

                spi_arr = np.array(spi_arr).reshape(main_arr.shape)
                print()

                print("Original Array:")
                print(main_arr)
                print()
                print("Second Array:")
                print(spi_arr)
                print()

                print("Combined Array (vertical stack):")

                if main_arr.ndim == 1:
                    new = np.concatenate((main_arr,spi_arr))
                else:
                    new = np.vstack((main_arr,spi_arr))

                print(new)
                print()

            elif cho == 2 :

                print()
                split_arr = int(input("Enter the number of splits : "))

                if split_arr <= 0:
                    print("Number of splits must be positive.")
                    return

                split_arr2 = np.array_split(main_arr,split_arr)
                print()
                print("Original Array:")
                print(main_arr)
                print()
                print("Splitted Array")

                for part in split_arr2:
                    print(part)

            else:
                print("Invalid choice ")

        except :
            print("Error")

    def search_arr(self,main_arr):
        
        try:

            print()
            print("Choose an option")
            print()
            print("1. Search a value")
            print("2. Sort the Array")
            print("3. Filter values")
            print()


            choice = int(input("Enter your choice :-  "))
            print()

            if choice==1:
                
                print()
                print("Original Array : ")
                print(main_arr)
                search=int(input("Enter a value to search:  "))
                print()
            
                if np.any(main_arr == search):

                    print()
                    
                    print("Value found At Index number ")
                    p=np.argwhere(main_arr==search)
                    
                    print(p)
                else:
                    
                    print("Value is not available")
            
            elif choice ==2:
                    
                    print()
                    print("Original Array")
                    print(main_arr)
                    print()
                    print("Sorted Array ")
                    print(np.sort(main_arr))
                    print()


            elif choice ==3:
                
                print()
                print("Choose an Option ")
                print()
                print("1. Values less-than")
                print("2. Values greater-than")
                print()
                option=int(input("Enter Your Choice :-"))
                
                if option == 1 :
                    
                    print()
                    less_arr=int(input("Enter a Value :"))
                    print()
                    print("Original Array")
                    print(main_arr)
                    print()
                    print("Filtered Array")
                    print(main_arr[main_arr<less_arr])
                    print()

                elif option==2:
                    
                    print()
                    greater_arr=int(input("Enter a Value :"))
                    print()
                    print("Original Array")
                    print(main_arr)
                    print()
                    print("Filtered Array")
                    print(main_arr[main_arr>greater_arr])
                    print()

                else:
                    print("Invalid choice")

            else:
                print("Invalid choice")

        except :
            print("Error")

    def agg_func(self,main_arr):
        
        try:
            
            print("-"*10,"Aggregates and Statistics","-"*10)
            print()
            print("Choose an Option ")
            print()
            print("1. Sum")
            print("2. Mean")
            print("3. Median")
            print()

            option=int(input("Enter your choice:  "))
            print()
            
            if option == 1 :
                
                print("Original Array :")
                print(main_arr)
                print("Sum of the Original array :")
                print(np.sum(main_arr))
                print()

            elif option == 2 : 

                print()
                print("Original Array :")
                print(main_arr)
                print()
                print("Mean of the Original Array:")
                print(np.mean(main_arr))
                print()


            elif option == 3 :

                print()
                print("Original Array :")
                print(main_arr)
                print()
                print("Median Of Original Array :")
                print(np.median(main_arr))
                print()
                
            else:
                
                print("Invalid Choice !!")

        except :
            print("Error:")


    def main_menu(self):
        
         print()
         print("="*52)
         print("========== Welcome to The NumPy Analyzer ===========")
         print("="*52)
         print()
        
         print("MAIN MENU - ")
         print()
         print("1. Create a Numpy Array ")
         print("2. Perform Mathematical Operations")
         print("3. Combine or split Arrrays")
         print("4. Search, Sort, or Filter Arrays")
         print("5. Compute Aggregates and Statistics")
         print("6. Exit")
         print()


    

    def start_prog(self):
         
    
         while True:
            
            self.main_menu() 

            try:
                option = int(input("Enter your choice:-  ")) 
            except :
                print("Please enter a valid number.")
                continue

            print()

            if option == 1 :
                
              main_arr = self.create_numpy()

            
            
            elif option == 2 :
                
                self.math_op(self.arr)
            
            elif option == 3 :
                
                

                self.combine_arr(self.arr)
            
            elif option == 4 :
                
                
                self.search_arr(self.arr)
            
            elif option == 5 :
                
                

                self.agg_func(self.arr)
            
            elif option == 6 :
                
                print("Exiting the Program....")
                print()
                print("Thanks for using the NumPy Analyzer! ")
                print("="*40*6)
                print()
                break

            else:
                print("Invalid choice. Please enter a number from 1 to 6.")


            
obj = data_analytics()
obj.start_prog()
