"""Customers at Hackbright."""

# Jane|Melonista|jane@jane.com|secret
# Jayden|Auden|jayden@gmail.com|nevertell
# Janet|Jefferson|janet@hotmail.com|seekrit

class Customer(object):
    """Ubermelon customer."""

    def __init__(self, 
                 first_name, 
                 last_name, 
                 email, 
                 password):

        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = password


    def __repr__(self):
        """Convenience method to show information about customer in console."""

        return (f"<Customer: {self.first_name} {self.last_name}, {self.email}>")


def make_customers():
    file = open('customers.txt')

    # need a dictionary
    # iterate over file
    # split at "|"
    # save info to dictionary
    # {
    #   email : Customer object(first_name, last_name, email, password)
    # }
    email_lookup = {}

    for line in file:
        line = line.rstrip()
        person_section = line.split("|")
        person_email = person_section[2]
        email_lookup[person_email] = Customer(person_section[0], person_section[1], person_section[2], person_section[3])

    return email_lookup



def get_by_email(email):

    # use email_lookup
    # return object from email (which is the key)
    # email_lookup = make_customers()

    return make_customers()[email]

    


if __name__ == "__main__":
# to avoid running it as an import

    customer_dict = make_customers()
    #this runs make_customers() as customer_dict as long as it is 
    #run directly on command line

    print("I'm running! This is __main__!")