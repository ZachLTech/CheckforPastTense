use rsnltk::tokenize::word_tokenize;
use rsnltk::tag::pos_tag;
use std::collections::HashSet;
use std::fs::File;
use std::io::{BufRead, BufReader};

fn main() {
    // Load English verbs
    let english_verbs: HashSet<String> = rsnltk::wordnet::verb::all_lemma_names()
        .iter()
        .map(|w| w.to_lowercase())
        .collect();

    // Load past tense verbs
    let past_tense_verbs: HashSet<String> = {
        let file = File::open("filteredpasttense.txt").expect("Failed to open file");
        let reader = BufReader::new(file);
        reader
            .lines()
            .map(|line| line.expect("Failed to read line"))
            .map(|w| w.to_lowercase())
            .collect()
    };

    // Load input file
    let file = File::open("checkf.txt").expect("Failed to open file");
    let reader = BufReader::new(file);
    let mut non_past_tense_verbs: Vec<String> = vec![];
    for line in reader.lines() {
        let words: Vec<&str> = word_tokenize(&line.expect("Failed to read line")).into_iter().map(|w| w.as_ref()).collect();
        let tagged_words = pos_tag(&words);
        for (word, tag) in tagged_words.iter() {
            if tag.starts_with('V') && !past_tense_verbs.contains(&word.to_lowercase()) && english_verbs.contains(&word.to_lowercase()) {
                non_past_tense_verbs.push(word.to_owned());
            }
        }
    }

    // Print results
    println!("The following English verbs are not in the past tense:");
    for verb in non_past_tense_verbs {
        println!("{}", verb);
    }
}