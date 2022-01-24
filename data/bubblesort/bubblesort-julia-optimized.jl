function swap_vector(vec_in, passes)
    no_swaps = 0
    for vec_index in 1:(length(vec_in) - 1 - passes)
        if vec_in[vec_index] > vec_in[vec_index + 1]
            no_swaps += 1
            tmp = vec_in[vec_index]
            vec_in[vec_index] = vec_in[vec_index + 1]
            vec_in[vec_index + 1] = tmp
        end
    end
    return no_swaps
end
function sort_julia(vec_in)
    passes = 0
    while(true)
        no_swaps = swap_vector(vec_in, passes)
        if no_swaps == 0
            break
        end
        passes += 1
    end
    return vec_in
end

# Parameter fuer Zufallszahlengenerator setzen.
const MIN_VALUE = -1000
const MAX_VALUE = 1000
const QUANTITY = 10000

# Zufallszahlen erstellen
random_numbers = rand(MIN_VALUE:0.000000000000001:MAX_VALUE, QUANTITY)

# Zufallszahlen sortieren, Ausfuehrungsdauer messen und Dauer in Konsole ausgeben.
# print("Duration: ")
# print(@elapsed bubblesort(random_numbers))
sort_julia(random_numbers)