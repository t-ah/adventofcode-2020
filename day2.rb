counts = [0,0]
File.read("day2.txt").split("\n").each do |line|
    from, to, letter, pw = line.match(/(\d+)-(\d+) (\w): (\w+)/i).captures
    letter_count = pw.count letter
    
    if letter_count >= from.to_i and letter_count <= to.to_i then
        counts[0] += 1
    end

    if (pw[from.to_i - 1] == letter) ^ (pw[to.to_i - 1] == letter) then
        counts[1] += 1
    end
end
puts counts