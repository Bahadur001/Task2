
# task_1
# def ededler(myList):
#     print([(num, int(num ** 0.5)) for num in myList if num >= 0 and int(num ** 0.5) ** 2 == num])

# myList = [-4, -16, 0, 1, 4, 5, 9, 16, 25, 36, 49, 64, 81, 100]
# ededler(myList)


# task_2
# def təkrar(myList):
#     return [num for num in myList if myList.count(num) == 1]
# list = [-1, 1, 2, 2, 6, 7, 7, 8, 9, 9]
# print("tekrar etmeyen ededler:", təkrar(list))


# task3
# def hesabla():
#     myList = input("ededler girin: ").split(",")
#     myList = [int(x.strip()) for x in myList]
#     if len(myList) == 0:
#         return 0
#     hasil = 1
#     for num in myList:
#         hasil *= num
#     return hasil
# print(" girilen ededlerin hasili:", hesabla())



# task4

# def bolen(num):
#     return [x for x in range(1, num + 1) if num % x == 0]
# num = 12
# print(bolen(num))

# task5
# aylar = ['Yanvar', 'Fevral', 'Mart', 'Aprel', 'May', 'İyun', 'İyul', 'Avqust', 'Sentyabr', 'Oktyabr', 'Noyabr', 'Dekabr']
# ay_uzunluq = {ay: len(ay) for ay in aylar}
# print(ay_uzunluq)

# task6
# names = ["Rick Sanchez", "Morty Smith", "Summer Smith", "Jerry Smith", "Beth Smith"]
# def adlari_getir(names):
#     return [name.split()[0].lower() for name in names]
# adlar = adlari_getir(names)
# print(adlar)


# task7
# nums1 = [1, 2, 3]
# nums2 = [4, 5, 6]

# ortalama = [(nums1[i] + nums2[i]) / 2 for i in range(min(len(nums1), len(nums2)))]

# print(ortalama)
