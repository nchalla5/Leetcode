type Stack struct {
    data []rune
}

func (s *Stack) Push(x rune) {
    s.data = append(s.data, x)
}

func (s *Stack) Empty() bool {
    return len(s.data) == 0
}

func (s *Stack) Pop() rune {
    top := s.data[len(s.data)-1]
    s.data = s.data[:len(s.data)-1]
    return top
}

func isValid(s string) bool {
    stack := Stack{}
    for _, c := range s {
        if c == '(' || c == '{' || c == '[' {
            stack.Push(c)
        } else if stack.Empty() {
            return false
        } else {
            pop := stack.Pop()
            if ((c == ')' && pop == '(') ||( c == '}' && pop == '{')||( c == ']' && pop == '[')) {
                
            } else {
                return false
            }
        }
        // fmt.Println(stack.data)
    }
    if stack.Empty() {
        return true
    }
    return false
}