pub fn parse(lines: &Vec<&str>) -> Vec<i32> {
    let mut values: Vec<i32> = vec![0; lines.len()];
    for index in 0..lines.len() {
        values[index] = lines[index].parse().unwrap();
    }
    return values;
}

pub fn compute_answer(lines: &Vec<&str>) -> i32 {
    let mut result: i32 = 0;
    let depths = parse(&lines);
    for index in 3..depths.len() {
        if depths[index] > depths[index - 3] {
            result += 1
        }
    }
    return result;
}
