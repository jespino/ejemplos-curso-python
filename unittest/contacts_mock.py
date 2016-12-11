import mock

def invite_user(address_book, name):
    print "Inviting user %s" % name
    address = address_book.get(name)
    # Code that invites the user
    print "Sending invitation to %s" % address


address_book = mock.Mock()
address_book.get.return_value = "jespinog@gmail.com"

invite_user(address_book, "jespino")
