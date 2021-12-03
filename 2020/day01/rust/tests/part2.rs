use advent::part2::*;

use std::str::FromStr;

#[test]
fn test_compute_answer_sample() {
    let lines = vec!["1721", "979", "366", "299", "675", "1456"];
    let target = 2020;
    let actual = compute_answer(&lines, target);
    let expected: i32 = 241861950;
    assert_eq!(actual, expected);
}

// Borrowed from: https://dev.to/dandyvica/different-ways-of-reading-files-in-rust-2n30
// Borrowed from: https://stackoverflow.com/questions/36020110/how-do-i-avoid-unwrap-when-converting-a-vector-of-options-or-results-to-only-the
fn get_lines<T: FromStr>(filename: &str) -> Vec<T> {
    std::fs::read_to_string(filename)
        .expect("file not found!")
        .lines()
        .map(|x| x.parse())
        .collect::<Vec<Result<T, <T as FromStr>::Err>>>()
        .into_iter()
        .filter_map(|e| e.ok())
        .collect()
}

#[test]
fn test_compute_answer_full() {
    let lines = get_lines::<String>("../data/input.dat");
    // Vec<String> => Vec<&str>
    let lines: Vec<&str> = lines.iter().map(|x| x.as_ref()).collect();
    let target = 2020;
    let actual = compute_answer(&lines, target);
    let expected: i32 = 32858450;
    assert_eq!(actual, expected);
}
