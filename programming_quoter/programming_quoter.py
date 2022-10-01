from win10toast import ToastNotifier
import random

listOfQuotes = ['First, solve the problem. '
                'Then, write the code',
                'Experience is the name everyone '
                'gives to their mistakes',
                'In order to be irreplaceable, '
                'one must always be different',
                'Java is to JavaScript '
                'what car is to Carpet',
                'Knowledge is power',
                'Ruby is rubbish! PHP '
                'is phpantastic!',
                'Code is like humor.'
                ' When you have to explain it, it’s bad',
                'Fix the cause, '
                'not the symptom',
                'Simplicity is the '
                'soul of efficiency',
                'Before software can be '
                'reusable it first has to be usable',
                'Make it work, make '
                'it right, make it fast',
                'Truth can only be found '
                'in one place: the code',
                'How you look at it is pretty '
                'much how youll see it',
                'Perl – The only language that '
                'looks the same before and after RSA encryption',
                'A conscious human is driven by '
                'their conscience, not popular opinion',
                'The most important property of a '
                'program is whether it accomplishes '
                'the intention of its user',
                'Computers are useless.  They '
                'can only give you answers',
                'Hardware: The parts of a '
                'computer system that can be kicked']

toaster = ToastNotifier()

toaster.show_toast("Programming Quote", random.choice(listOfQuotes),
                   icon_path=None,
                   duration=10)
