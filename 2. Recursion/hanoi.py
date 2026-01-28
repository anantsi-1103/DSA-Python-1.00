# def tower_of_hanoi(n,src,helper,dest):
#     if n == 1:
#         print(f"Move disk 1 from {src} to {dest}")
#         return
#     # yehi logic
#     # 
#     #function call
#     tower_of_hanoi(n-1,src,dest,helper) #top wali disk ko source - helper
#     print(f"Move disk {n} from {src} to {dest}")
#     # last wali disk ko helper - dest
#     tower_of_hanoi(n-1,helper,src,dest)

#     # 2n - 2^n

def tower_of_hanoi(n, src, helper, dest):
    if n == 1:
        print(f"Move disk 1 from {src} to {dest}")
        return

    # Step 1: Move top n-1 disks from src → helper
    tower_of_hanoi(n-1, src, dest, helper)

    # Step 2: Move nth (largest) disk from src → dest
    print(f"Move disk {n} from {src} to {dest}")

    # Step 3: Move n-1 disks from helper → dest
    tower_of_hanoi(n-1, helper, src, dest)



n = 3
tower_of_hanoi(n,"Source","Helper","Destination")