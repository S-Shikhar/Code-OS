echo "Calculator"
echo "choose: 1. (+), 2. (-), 3. (*), 4. (/)"

read -p "Enter your Choice(1, 2, 3, 4): " c

case $c in
    1)
        read -p "Enter two numbers: " a b
        echo "$a + $b = $(($a + $b))"
        ;;
    2)
        read -p "Enter two numbers: " a b
        echo "$a - $b = $(($a - $b))"
        ;;
    3)
        read -p "Enter two numbers: " a b
        echo "$a * $b = $(($a * $b))"
        ;;
    4)
        read -p "Enter two numbers: " a b
        echo "$a / $b = $(($a / $b))"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac