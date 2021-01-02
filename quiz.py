import math
import random, time

# Node creation
class Node:
    def __init__(self, order):
        self.order = order
        self.values = []
        self.keys = []
        self.nextKey = None
        self.parent = None
        self.check_leaf = False

    # Insert at the leaf
    def insert_at_leaf(self, leaf, value, key):
        if self.values:
            temp1 = self.values
            for i in range(len(temp1)):
                if value == temp1[i]:
                    self.keys[i].append(key)
                    break
                elif value < temp1[i]:
                    self.values = self.values[:i] + [value] + self.values[i:]
                    self.keys = self.keys[:i] + [key] + self.keys[i:]
                    break
                elif i + 1 == len(temp1):
                    self.values.append(value)
                    self.keys.append(key)
                    break
        else:
            self.values = [value]
            self.keys = [key]


# B plus tree
class BplusTree:
    def __init__(self, order):
        self.root = Node(order)
        self.root.check_leaf = True

    # Insert operation
    def insert(self, value, key):
        value = str(value)
        old_node = self.search(value)
        old_node.insert_at_leaf(old_node, value, key)

        if (len(old_node.values) == old_node.order):
            node1 = Node(old_node.order)
            node1.check_leaf = True
            node1.parent = old_node.parent
            mid = int(math.ceil(old_node.order / 2)) - 1
            node1.values = old_node.values[mid + 1:]
            node1.keys = old_node.keys[mid + 1:]
            node1.nextKey = old_node.nextKey
            old_node.values = old_node.values[:mid + 1]
            old_node.keys = old_node.keys[:mid + 1]
            old_node.nextKey = node1
            self.insert_in_parent(old_node, node1.values[0], node1)

    # Search operation for different operations
    def search(self, value):
        current_node = self.root
        while current_node.check_leaf == False:
            temp2 = current_node.values
            for i in range(len(temp2)):
                if value == temp2[i]:
                    current_node = current_node.keys[i + 1]
                    break
                elif value < temp2[i]:
                    current_node = current_node.keys[i]
                    break
                elif i + 1 == len(current_node.values):
                    current_node = current_node.keys[i + 1]
                    break
        return current_node

    # Find the node
    def find(self, value, key):
        l = self.search(value)
        for i, item in enumerate(l.values):
            if item == value:
                if key in l.keys[i]:
                    return True
                else:
                    return False
        return False

    # Inserting at the parent
    def insert_in_parent(self, n, value, ndash):
        if (self.root == n):
            rootNode = Node(n.order)
            rootNode.values = [value]
            rootNode.keys = [n, ndash]
            self.root = rootNode
            n.parent = rootNode
            ndash.parent = rootNode
            return

        parentNode = n.parent
        temp3 = parentNode.keys
        for i in range(len(temp3)):
            if (temp3[i] == n):
                parentNode.values = parentNode.values[:i] + [value] + parentNode.values[i:]
                parentNode.keys = parentNode.keys[:i + 1] + [ndash] + parentNode.keys[i + 1:]
                if (len(parentNode.keys) > parentNode.order):
                    parentdash = Node(parentNode.order)
                    parentdash.parent = parentNode.parent
                    mid = int(math.ceil(parentNode.order / 2)) - 1
                    parentdash.values = parentNode.values[mid + 1:]
                    parentdash.keys = parentNode.keys[mid + 1:]
                    value_ = parentNode.values[mid]
                    if (mid == 0):
                        parentNode.values = parentNode.values[:mid + 1]
                    else:
                        parentNode.values = parentNode.values[:mid]
                    parentNode.keys = parentNode.keys[:mid + 1]
                    for j in parentNode.keys:
                        j.parent = parentNode
                    for j in parentdash.keys:
                        j.parent = parentdash
                    self.insert_in_parent(parentNode, value_, parentdash)

class Quiz:

    def __init__(self, ques_object, x):
        self.total_ques = x
        self.ques = ques_object
        self.rank = {'cat1':[], 'cat2':[], 'cat3':[], 'cat4':[], 'cat5':[],}

    def ratio_splitter(self, number):
        number = number // 20
        return [10*number, 4*number, 3*number, 2*number, number]

    def attempt(self):
        # Initializing Categories
        total = {'cat1':[0, 0, 0], 'cat2':[0, 0, 0], 'cat3':[0, 0, 0], 'cat4':[0, 0, 0], 'cat5':[0, 0, 0]}
        ratio = self.ratio_splitter(self.total_ques)
        category = list(total.keys())

        for j in range(len(ratio)):
            cat = category[j]
            for i in range(ratio[j]):
                ques = self.ques.search(str(i))
                index = ques.values.index(str(i))
                choices = ques.keys[index]
                answers = list(choices.values())[0]

                #print(f"Question {i+1}: {questions[0]}")
                #print(f"Choices: 1. {questions[1][0]}\t2. {questions[1][1]}\t3. {questions[1][2]}\t4. {questions[1][3]}")

                ans = random.choice(answers[0])
                questions = list(choices.keys())[0]

                if int(ans) in answers[1]:
                    #print("\nCorrect")
                    total[cat][0] += 1
                else:
                    #print("\nIncorrect")
                    total[cat][1] += 1
                    total[cat][2] = total[cat][0] - (total[cat][1] * 0.5)

            self.rank[cat].append(total[cat][2])

        return self.rank


if __name__ == '__main__':

    record_len = 4
    bplustree = BplusTree(record_len)

    # Temporary block of Code for Creating questions answers for quiz
    X = int(input("Enter your Date of Birth: "))
    X -= (X % 20)
    list2 = []

    print("Creating Questions. This is not the part of problem actually...")
    t1 = time.time()
    for i in range(X):
        ans_list = []
        que_dict = {}
        correct_answers = []

        ans_list = [random.randint(1, 100) for j in range(4)]

        correct_answers = [random.choice(ans_list) for n in range(random.randint(1, 3))]

        q = 'q' + str(i)
        que_dict[q] = [ans_list, correct_answers]

        list2.append(que_dict)
        # print(que_dict)

    t2 = time.time()
    print("calculate time from now on :)")

    t3 = time.time()
    for i in range(len(list2)):
        bplustree.insert(str(i), list2[i])

    st = Quiz(bplustree, len(list2))

    student_no = int(input("Enter the Number of Students"))
    for j in range(student_no):
        # Appending the marks of Student in overall students result
        students = st.attempt()

    t4 = time.time()

    print(t4-t3)

    for cat in students.keys():
        temp = students[cat]
        toppers = []
        for i in range(5):
            toppers.append(max(temp))
            temp.remove(toppers[-1])
        print(cat, toppers)
