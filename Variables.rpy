init 10 python:
    import requests
    import json
    class Variables():
        def __init__(self):
            self._award_points = 5
            self._penalty_points = 2
            self._max_penalty_times = 2
            self.points = 0
            self._mistakes = 0
            self.retry_option = False
            self.continue_anyway = False
            self.leaderboard = self.load_leaderboard()
            self._wrong_answers = {}
            self._pages = 0
            self._max_pages = 4

        @property
        def mistakes(self):
            return self._mistakes
        @mistakes.setter
        def mistakes(self, value):
            self._mistakes = value
            if self._mistakes > 2:
                self.retry_option = True

        def correct_answer(self, question_id):
            '''
            Awards points to player for answering the question correctly.
            If the question was previously answered incorrectly, the player
            will be awarded the points minus the penalty points for each
            incorrect answer.

            :param question_id: The ID of the question that was answered correctly.
            '''
            # Get the number of times the question was answered incorrectly
            incorrect_answered = self._wrong_answers.get(question_id, 0)
            self.points += (
                # Award points for correct answer
                self._award_points - 
                # Subtract points for each incorrect answer
                # but not more than 2 times
                min(incorrect_answered, self._max_penalty_times) * self._penalty_points
            )
            # Remove the question from the wrong answers list
            # so that it's not asked again, till the player answersed
            # all questions correctly
            if question_id in self._wrong_answers:
                del self._wrong_answers[question_id]

        def wrong_answer(self, question_id):
            '''
            Adds wrong answer to wrong answers list, so that we can
            keep track of how many times a question was answered incorrectly.

            :param question_id: The ID of the question that was answered incorrectly.
            '''
            self.mistakes += 1
            self._wrong_answers.update({
                question_id: self._wrong_answers.get(question_id, 0) + 1
            })

        @property
        def wrong_answers(self):
            return self._wrong_answers.keys()

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


