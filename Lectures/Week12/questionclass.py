class Question :
  def __init__(self) :
    self._text = ""
    self._answer = ""

  def setText(self, question_text):
    self.text = question_text

  def setAnswer(self, correct_answer):
    self._answer = correct_answer

  def checkAnswer(self, response):
    return response == self._answer

  def display(self) :
    print(self.text)

class ChoiceQuestion(Question):
    def __init__(self):
        super().__init__()
        self._choices = []

    def addChoice(self, choice, correct):
        self._choices.append(choice)
        if correct:
           choiceString = str(len(self._choices))
           self.setAnswer(choiceString)
    
    def display(self):
        super().display()
    
        for i in range(len(self._choices)):
           choiceNumber = i + 1
           print("%d: %s" % (choiceNumber, self._choices[i]))

def main():
    q1 = ChoiceQuestion()

    q1.setText("In which country was the inventor of Python born? ")
    q1.addChoice("Australia", False)
    q1.addChoice("China", False)
    q1.addChoice("Netherland", True)
    q1.addChoice("USA", False)
    q1.addChoice("Japan", False)
    q1.addChoice("Isreal", False)
    q1.addChoice("UK", False)
    q1.display()
    response = input("What is your answer?")
    print(q1.checkAnswer(response))

if __name__ == "__main__":
   main()
          
          



