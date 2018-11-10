def format_zipcode(zip_code):

    if len ( zip_code ) <= 5: print '{:<05}'.format ( zip_code )
    if len ( zip_code ) == 10: print str ( zip_code )
    if len ( zip_code ) == 9: print '{}-{}'.format ( zip_code[:5], zip_code[5:] )


format_zipcode('')
format_zipcode('1234556789')
format_zipcode('123456789')


'''
test scenarios : 
1.For the given input length is les than or equal to 5 then we should format  the input by prefix 0 till the length equals to 5.
2.for the given input if the length is equal to 10 then display as it is
3.for the  given input if the length is of 9 , then output should be formatted as seperate first 5 digits and remaining with '-'
4.for any other length zipcode input there should not be any output.
'''
