python todo.py add "Buy groceries" --description "Milk, eggs, bread" --due "2025-11-15"

python todo.py add "Finish project report" --description "Due for client" --due "2025-11-13"

python todo.py add "Workout" --description "Morning gym" 

python todo.py add "Call mom"


python todo.py list


python todo.py list --sort date


python todo.py list --sort created

python todo.py list --completed

python todo.py list --pending

python todo.py done 2

python todo.py list

python todo.py edit 3 --title "Evening Workout" --due "2025-11-20"

python todo.py edit 1 --description "Buy fruits and vegetables too"

python todo.py delete 4

python todo.py delete 3 --force

python todo.py search "project"

python todo.py search "Buy"

python todo.py clear

python todo.py clear --force

python todo.py list
