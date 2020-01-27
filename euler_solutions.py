from calculations import *

# Problem 1
total_sum = 0
for i in range(0, 1000):
    if not i % 3 or not i % 5:
        total_sum += i

print(total_sum)

# Problem 2
n = 1
total_sum = 0
while fib_no_recursion(n) <= 4000000:
    if fib_no_recursion(n) % 2 == 0:
        total_sum += fib_no_recursion(n)
    n += 1
print(total_sum)

# Problem 3
max_prime_factor(600851475143)

# Problem 4
current_num = 0
largest_palindrome = 0
for i in range(10, 100):
    for j in range(10, 100):
        current_num = (i * j)
        is_palindrome = check_for_palindrome(current_num)
        if is_palindrome and current_num > largest_palindrome:
            largest_palindrome = current_num

print(largest_palindrome)

# Problem 5
num = 20
is_target = False
divisors = list(range(1, 21))
while not is_target:
    for i in divisors:
        if(num % 2 or num % 3 or num % 4 or num % 5 or num % 6 or num % 7 or num % 8 or num % 9 or num % 10 or num % 11
                or num % 12 or num % 13 or num % 14 or num % 15 or num % 16 or num % 17 or num % 18 or num % 19
                or num % 20):
            num += 1
        else:
            is_target = True
print(num)

# Problem 6
sum_of_square = 0
square_of_sum = 0
difference = 0
_sum = 0
for i in range(101):
    sum_of_square += i ** 2

for i in range(101):
    _sum += i

square_of_sum = _sum ** 2
difference = square_of_sum - sum_of_square
print(difference)

# Problem 7
count = 0
current_number = 0
while count != 10001:
    num_is_prime = is_prime(current_number)
    if num_is_prime:
        count += 1
    if count == 10001:
        print(current_number)
    current_number += 1

# Problem 8
s = """7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891
       1294949545950173795833195285320880551112540698747158523863050715693290963295227443043557668966489504452445231617
       3185640309871112172238311362229893423380308135336276614282806444486645238749303589072962904915604407723907138105
       1585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522
       4352584907711670556013604839586446706324415722155397536978179778461740649551492908625693219784686224828397224137
       5657056057490261407972968652414535100474821663704844031998900088952434506585412275886668811642717147992444292823
       0863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421
       7506941658960408071984038509624554443629812309878799272442849091888458015616609791913387549920052406368991256071
       76060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"""

largestProduct = 0

for i in range(0, len(s) - 13):

    product = 1

    for j in range(i, i + 13):
        product *= int(s[j: j + 1])

    if product > largestProduct:
        largestProduct = product

print(largestProduct)

# Problem 9
num_list = range(1, 1000)
special_triplet = False

for a in num_list:
    for b in range(a, 1000 - a):
        for c in range(b, 1000 - b):
            if a + b + c == 1000:
                if a ** 2 + b ** 2 == c ** 2:
                    special_triplet = True
                    print(a * b * c)
                    print(a, b, c)
                else:
                    special_triplet = False

# Problem 10
sum_of_primes = 0

for i in range(2000000):
    prime_check = is_prime(i)
    if prime_check:
        sum_of_primes += i

print(sum_of_primes)

# Problem 11
# Solved by guess and check

# Problem 12
triangle_number_n = 0
i = 1

while num_factors(triangle_number_n) < 500:
    triangle_number_n += i
    i += 1

print(triangle_number_n)

# Problem 13
numbers_list = [37107287533902102798797998220837590246510135740250,
                46376937677490009712648124896970078050417018260538,
                74324986199524741059474233309513058123726617309629,
                91942213363574161572522430563301811072406154908250,
                23067588207539346171171980310421047513778063246676,
                89261670696623633820136378418383684178734361726757,
                28112879812849979408065481931592621691275889832738,
                44274228917432520321923589422876796487670272189318,
                47451445736001306439091167216856844588711603153276,
                70386486105843025439939619828917593665686757934951,
                62176457141856560629502157223196586755079324193331,
                64906352462741904929101432445813822663347944758178,
                92575867718337217661963751590579239728245598838407,
                58203565325359399008402633568948830189458628227828,
                80181199384826282014278194139940567587151170094390,
                35398664372827112653829987240784473053190104293586,
                86515506006295864861532075273371959191420517255829,
                71693888707715466499115593487603532921714970056938,
                54370070576826684624621495650076471787294438377604,
                53282654108756828443191190634694037855217779295145,
                36123272525000296071075082563815656710885258350721,
                45876576172410976447339110607218265236877223636045,
                17423706905851860660448207621209813287860733969412,
                81142660418086830619328460811191061556940512689692,
                51934325451728388641918047049293215058642563049483,
                62467221648435076201727918039944693004732956340691,
                15732444386908125794514089057706229429197107928209,
                55037687525678773091862540744969844508330393682126,
                18336384825330154686196124348767681297534375946515,
                80386287592878490201521685554828717201219257766954,
                78182833757993103614740356856449095527097864797581,
                16726320100436897842553539920931837441497806860984,
                48403098129077791799088218795327364475675590848030,
                87086987551392711854517078544161852424320693150332,
                59959406895756536782107074926966537676326235447210,
                69793950679652694742597709739166693763042633987085,
                41052684708299085211399427365734116182760315001271,
                65378607361501080857009149939512557028198746004375,
                35829035317434717326932123578154982629742552737307,
                94953759765105305946966067683156574377167401875275,
                88902802571733229619176668713819931811048770190271,
                25267680276078003013678680992525463401061632866526,
                36270218540497705585629946580636237993140746255962,
                24074486908231174977792365466257246923322810917141,
                91430288197103288597806669760892938638285025333403,
                34413065578016127815921815005561868836468420090470,
                23053081172816430487623791969842487255036638784583,
                11487696932154902810424020138335124462181441773470,
                63783299490636259666498587618221225225512486764533,
                67720186971698544312419572409913959008952310058822,
                95548255300263520781532296796249481641953868218774,
                76085327132285723110424803456124867697064507995236,
                37774242535411291684276865538926205024910326572967,
                23701913275725675285653248258265463092207058596522,
                29798860272258331913126375147341994889534765745501,
                18495701454879288984856827726077713721403798879715,
                38298203783031473527721580348144513491373226651381,
                34829543829199918180278916522431027392251122869539,
                40957953066405232632538044100059654939159879593635,
                29746152185502371307642255121183693803580388584903,
                41698116222072977186158236678424689157993532961922,
                62467957194401269043877107275048102390895523597457,
                23189706772547915061505504953922979530901129967519,
                86188088225875314529584099251203829009407770775672,
                11306739708304724483816533873502340845647058077308,
                82959174767140363198008187129011875491310547126581,
                97623331044818386269515456334926366572897563400500,
                42846280183517070527831839425882145521227251250327,
                55121603546981200581762165212827652751691296897789,
                32238195734329339946437501907836945765883352399886,
                75506164965184775180738168837861091527357929701337,
                62177842752192623401942399639168044983993173312731,
                32924185707147349566916674687634660915035914677504,
                99518671430235219628894890102423325116913619626622,
                73267460800591547471830798392868535206946944540724,
                76841822524674417161514036427982273348055556214818,
                97142617910342598647204516893989422179826088076852,
                87783646182799346313767754307809363333018982642090,
                10848802521674670883215120185883543223812876952786,
                71329612474782464538636993009049310363619763878039,
                62184073572399794223406235393808339651327408011116,
                66627891981488087797941876876144230030984490851411,
                60661826293682836764744779239180335110989069790714,
                85786944089552990653640447425576083659976645795096,
                66024396409905389607120198219976047599490197230297,
                64913982680032973156037120041377903785566085089252,
                16730939319872750275468906903707539413042652315011,
                94809377245048795150954100921645863754710598436791,
                78639167021187492431995700641917969777599028300699,
                15368713711936614952811305876380278410754449733078,
                40789923115535562561142322423255033685442488917353,
                44889911501440648020369068063960672322193204149535,
                41503128880339536053299340368006977710650566631954,
                81234880673210146739058568557934581403627822703280,
                82616570773948327592232845941706525094512325230608,
                22918802058777319719839450180888072429661980811197,
                77158542502016545090413245809786882778948721859617,
                72107838435069186155435662884062257473692284509516,
                20849603980134001723930671666823555245252804609722,
                53503534226472524250874054075591789781264330331690]
total_sum = 0

for i in numbers_list:
    total_sum += i

sum_as_string = str(total_sum)
print(sum_as_string[:10])

# Problem 14
num_longest = 0
longest_sequence = 0

for i in range(1000000):
    length_of_sequence = collatz_sequence(i)
    if length_of_sequence > longest_sequence:
        longest_sequence = length_of_sequence
        num_longest = i

print(num_longest)

# Problem 15
num_paths = 0
a = 20
b = 20
binomial_coeff = factorial(a + b) / (factorial(a) * factorial(b))

print(binomial_coeff)

# Problem 16
to_sum = str(2 ** 1000)
digit_sum = 0

for i in range(len(to_sum)):
    digit_sum += int(to_sum[i])

print(digit_sum)

# Problem 17
S = [0, 3, 3, 5, 4, 4, 3, 5, 5, 4, 3, 6, 6, 8, 8, 7, 7, 9, 8, 8]
D = [0, 3, 6, 6, 5, 5, 5, 7, 6, 6]
H = 7
T = 8

total = 0
for i in range(1, 1000):
    c = int(i % 10)  # singles digit
    b = int(((i % 100) - c) / 10)  # tens digit
    a = int(((i % 1000) - (b * 10) - c) / 100)  # hundreds digit

    if int(a) != 0:
        total += S[a] + H  # "S[a] hundred
        if int(b) != 0 or int(c) != 0:
            total += 3  # "and"
    if int(b) == 0 or int(b) == 1:
        total += S[b * 10 + c]
    else:
        total += D[b] + S[c]

total += S[1] + T

print(total)

# Problem 18
number = '''
75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

num_list = number.strip().split('\n')

for i in range(len(num_list)):
    num_list[i] = num_list[i].strip().split(' ')
    num_list[i] = [int(x) for x in num_list[i]]

num_list[0] = [75]

for i in range(len(num_list)-2, -1, -1):
    for j in range(len(num_list[i])):
        num_list[i][j] = num_list[i][j] + max(num_list[i+1][j], num_list[i+1][j+1])

    num_list.pop()

print(num_list[0][0])

# Problem 19
print((1/7) * 100 * 12)

# Problem 20
sum_of_digits = 0
n = 100
factorial_value = str(recursive_factorial(n))
for i in range(len(factorial_value)):
    sum_of_digits += int(factorial_value[i])

print(sum_of_digits)

# Problem 21
total_sum = 0
for i in range(1, 10001):
    sum1 = sum(get_factors(i))
    sum2 = sum(get_factors(sum1))
    if sum2 == i and sum1 != i:
        total_sum += i
print(total_sum)

# Problem 22
letter_values = {'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5, 'F': 6, "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
                 "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17, "R": 18, "S": 19, "T": 20, "U": 21, "V": 22, "W": 23,
                 "X": 24, "Y": 25, "Z": 26}
names_file = open("p022_names.txt", 'r')
names_list = names_file.readlines()
names_string = names_list[0]
names_list = names_string.split(',')
sorted_names_list = names_list
sorted_names_list.sort()
name_sum = 0
total_names_sum = 0

for i in range(len(sorted_names_list)):
    sorted_names_list[i] = sorted_names_list[i].strip('"')

for name in range(len(sorted_names_list)):
    name_sum = 0
    for i in range(len(sorted_names_list[name])):
        current_letter = sorted_names_list[name][i].capitalize()
        name_sum += letter_values[current_letter]
        print(name_sum)
    total_names_sum += name_sum * (name + 1)

print(total_names_sum)

# Problem 23
current_num = 0
abundant_nums = []
non_abundant_sum = 0
abundant_sums = []
abundant_total = 0
for i in range(1, 28123):
    if i < sum(get_factors(i)):
        abundant_nums.append(i)
print(type(abundant_nums))

for num in range(len(abundant_nums)//2):
    for num2 in range(len(abundant_nums) - 1, num - 1, -1):
        if (abundant_nums[num] + abundant_nums[num2]) not in abundant_sums \
                and (abundant_nums[num] + abundant_nums[num2]) < 28123:
            abundant_sums.append(abundant_nums[num] + abundant_nums[num2])
            abundant_total += abundant_nums[num] + abundant_nums[num2]
            print(abundant_nums[num] + abundant_nums[num2])

for j in range(1, 28123):
    non_abundant_sum += j

print(non_abundant_sum - abundant_total)

# Problem 24

# Problem 25
fib_length = 0
index = 1

while fib_length < 1000:
    index += 1
    nth_term = fib_no_recursion(index)
    fib_length = len(str(nth_term))

print(index)

# Problem 28
addend = 2
loop = 1
to_add = 3
total = 1

for square in range(1, 501):
    addend = 2 * square

    while loop < 4:
        total += to_add
        to_add += addend
        print(total, loop, to_add, addend)
        loop += 1

    loop = 0

print(total + to_add)
