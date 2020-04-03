    def Print_Buy_Requests(self):
        print(c.databaseTableBuyRequests)
        buyRequests = self.Get_Buy_Requests()

        for buyRequest in buyRequests:
            print(buyRequest)

        print('')

