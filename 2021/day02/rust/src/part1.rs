struct Position {
    hpos: i32,
    depth: i32,
}

pub fn parse_line(line: &str) -> (&str, i32) {
    let tokens: Vec<&str> = line.split(" ").collect();
    let dir = tokens[0];
    let amt = tokens[1].parse().unwrap();
    return (dir, amt);
}

pub fn compute_answer(lines: &Vec<&str>) -> i32 {
    let mut pos = Position { hpos: 0, depth: 0 };
    for index in 0..lines.len() {
        let (dir, amt) = parse_line(lines[index]);
        match dir {
            "forward" => pos.hpos += amt,
            "down" => pos.depth += amt,
            "up" => pos.depth -= amt,
            _ => panic!("Unknown direction: {}", dir),
        }
    }
    if pos.depth < 0 {
        panic!("Invalid depth: {}", pos.depth);
    }
    return pos.hpos * pos.depth;
}
