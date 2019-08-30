class Solution(object):
    def invalidTransactions(self, transactions):
        """
        :type transactions: List[str]
        :rtype: List[str]
        """
        parsed=[]
        invalidReturn=set()
        #get out of string form
        for transaction in transactions:
            parsed.append(transaction.split(","))
            
        #see if spent > 1000
        for i, moneyParse in enumerate(parsed):
            if int(moneyParse[2]) > 1000:
                invalidReturn.add(transactions[i])
        #See if same name
        for i, personParse in enumerate(parsed):
            lowTime=int(personParse[1])-60
            highTime=int(personParse[1])+60
            for j, secondPersonParse in enumerate(parsed):
                #see if different cities
                if personParse[0] == secondPersonParse[0] and j != i and (personParse[3] !=secondPersonParse[3]):
                        if int(secondPersonParse[1]) in range(lowTime, highTime):
                            if transactions[i] not in invalidReturn:                 
                                invalidReturn.add(transactions[i])
                            if transactions[j] not in invalidReturn:
                                invalidReturn.add(transactions[j])
        return invalidReturn
