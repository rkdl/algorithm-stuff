function isLAlpha(char) {
    const chCode = char.charCodeAt(0);
    return chCode >= 'a'.charCodeAt(0) && chCode <= 'z'.charCodeAt(0);
}

function splitIntoWords(document) {
    const words = [];
    let word = [];
    for (const char of document) {
        const lChar = char.toLowerCase();
        if (lChar === ' ' && word.length > 0) {
            words.push(word.join(''));
            word = [];    
        } else if (isLAlpha(lChar)) {
            word.push(lChar);
        }
    }
    if (word.length > 0) {
        words.push(word.join(''));
    }

    return words;
}

function wordCountEngine(document) {
    const words = splitIntoWords(document);

    let maxOccurances = 0;
    const map = new Map(); // Map<string, number>
    for (const word of words) {
        const occurances = map.has(word)
            ? map.get(word) + 1
            : 1;
        map.set(word, occurances);
        if (occurances > maxOccurances) {
            maxOccurances = occurances;
        }
    }

    const buckets = new Array(maxOccurances + 1);
    buckets.fill(null);

    for (const [word, occurances] of map.entries()) {
        let bucket = buckets[occurances];
        if (bucket === null) {
            bucket = [];
            buckets[occurances] = bucket;
        }
        bucket.push(word);
    }

    const result = [];
    for (let i = buckets.length - 1; i >= 0; i--) {
        const words = buckets[i];
        if (words === null) {
          continue;
        }
        for (const word of words) {
          result.push([word, i.toString()]);
        }
    }

    return result;
}
