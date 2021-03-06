function bubblesort!(arr::AbstractVector)
    for _ in 2:length(arr), j in 1:length(arr)-1
        if arr[j] > arr[j+1]
            arr[j], arr[j+1] = arr[j+1], arr[j]
        end
    end
    return arr
end
 
v = rand(-1000:1000, 10000)
bubblesort!(v)
# println("# unordered: $v\n -> ordered: ", bubblesort!(v))
