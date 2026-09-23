class MinStack {
    vector<int> mStack;
    vector<int> minStack;
    int currMin = 0;

public:
    MinStack() {
        
    }
    
    void push(int val) {
        if (mStack.empty()){
            mStack.push_back(val);
            currMin = val;
            minStack.push_back(currMin);
            return;
        }

        mStack.push_back(val);
        currMin = min(currMin, val);
        minStack.push_back(currMin);
    }
    
    void pop() {
        mStack.pop_back();
        minStack.pop_back();
        if (!minStack.empty()) {
            currMin = minStack.back();
        }
    }
    
    int top() {
        return mStack.back();
    }
    
    int getMin() {
        return minStack.back();
    }
};
