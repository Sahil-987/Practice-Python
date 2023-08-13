student_info_dict = {
    1 : {
        "name" : "akash mishra 1",
        "gender" : "male",
        "address" : 'gumti'
    },

    2 : {        
        "name" : "akash mishra 2",
        "gender" : "male",
        "address" : 'sharda nagar'
    },

    3 : {
        "name" : "harshita shukla",
        "gender" : "female",
        "address" : "vijay nagar"
    }
}


def gender_prefix(func):
    def main(roll_no):
        result = func(roll_no)
        if result['gender'] == 'male':
            result['name'] = 'Mr. ' + result['name']
        else : 
            result['name'] = 'Ms. ' + result['name']

        return result
    return main


@gender_prefix
def student_info(roll_no):
    return student_info_dict[roll_no]




if __name__ == "__main__":
    print(student_info(1))
    print(student_info(2))
    print(student_info(3))
