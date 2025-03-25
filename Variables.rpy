init 10 python:
    import requests
    import json
    class Variables():
        def __init__(self):
            self._points = 0
            self._mistakes = 0
            self.retry_option = False
            self.continue_anyway = False
            self.leaderboard = self.load_leaderboard()

        @property
        def points(self):
            return self._points
        @points.setter
        def points(self, value):
            if value < self._points:
                self.mistakes += 1
            self._points = value

            
        @property
        def mistakes(self):
            return self._mistakes
        @mistakes.setter
        def mistakes(self, value):
            self._mistakes = value
            if self._mistakes > 2:
                self.retry_option = True
        
        def get_api_data(self):
            api_url = "https://api.jsonbin.io/v3/b/67a6f945ad19ca34f8fbf243"
            api_key = "$2a$10$V71sdRkkKP535d9MYEZjeeE7wEfgjmulpHsHg7r6M8o.iLdDK2R8W"
            return api_url, api_key

        def load_leaderboard(self):
            api_url, api_key = self.get_api_data()

            headers = {
                "X-Master-Key": api_key
            }
            
            response = requests.get(api_url, headers=headers)
            
            if response.status_code == 200:
                data = response.json()
                return data.get("record", {}).get("leaderboard", {})
            else:
                print("Error loading leaderboard:", response.text)
                return {}
        
        def save_leaderboard(self):
            api_url, api_key = self.get_api_data()
            
            headers = {
                "Content-Type": "application/json",
                "X-Master-Key": api_key
            }
            
            # GET request para hindi madelete existing data
            response = requests.get(api_url, headers=headers)
            if response.status_code == 200:
                existing_data = response.json().get("record", {})
                existing_leaderboard = existing_data.get("leaderboard", {})
                existing_leaderboard.update(self.leaderboard)  # Merge new scores with old ones
                
                # Top 5 Scores
                sorted_leaderboard = dict(sorted(existing_leaderboard.items(), key=lambda item: item[1], reverse=True)[:10])
                updated_data = {"leaderboard": sorted_leaderboard}
            else:
                print("Error retrieving existing leaderboard, creating new one.")
                updated_data = {"leaderboard": self.leaderboard}
            
            # PUT request para masave
            response = requests.put(api_url, headers=headers, json=updated_data)

            if response.status_code == 200:
                print("Leaderboard successfully updated!")
            else:
                print("Error saving leaderboard:", response.text)

        def reload_leaderboard(self):
            self.leaderboard = self.load_leaderboard()


#        @property
#        def playerpoints(self):
#            return self.points
#        
#        @playerpoints.setter
#        def playerpoints(self, value):  # Corrected setter name
#            self.points = value
#            if self.correct_choice:  # Added self reference
#                self.points += 5
    

#        def correct_choice(self, is_true):
#        if is_true:
#            self.points += 5
#        else:
#            self.points -= 1
#        @property
#        def playermistakes(self):
#            return self.mistakes
        
#        @playermistakes.setter
#        def playermistakes(self, value): #           self.mistakes = value
#           if self.incorrect_choice:  # Added self reference
#                self.mistakes += 1
        
#        @property
#        def mistakeschecker(self):
#            return self.mistakes_check
        
#        @mistakeschecker.setter
#        def mistakeschecker(self, value):  # Added value parameter
#            self.mistakes_check = value
#            if self.mistakes >= 2:
#                self.retry_option = True
#            else:
#                self.retry_option = False


