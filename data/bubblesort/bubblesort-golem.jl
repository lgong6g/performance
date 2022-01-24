using Random

# Ein nicht optimaler Bubble-Sort-Algorithmus. Nur fuer Benchmarkzwecke.
function bubblesort(some_numbers::AbstractVector)
    size = length(some_numbers)
    for _ in 1:size, j in 1:(size - 1)
        if some_numbers[j] > some_numbers[j + 1]
            some_numbers[j], some_numbers[j + 1] = some_numbers[j + 1], some_numbers[j]
        end
    end
    return some_numbers
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
bubblesort(random_numbers)