const wordCloud = require('../hash-tables/word-cloud.js')

test('String returns object of word frequency', () => {
    expect(wordCloud("After beating the eggs, Dana read the next step. The next step after was to cook the eggs"))
    .toStrictEqual({after:2,beating:1, the:4, eggs:2,dana:1,read:1,next:2,step:2, was:1,to:1,cook:1,});
  });

  test('Hypenated words allowed', () => {
    expect(wordCloud("After beating the eggs, Dana read the-next step. The-next step after was to cook the eggs"))
    .toStrictEqual({"after":2,beating:1, the:2, eggs:2,dana:1,read:1,step:2, "the-next":2,was:1,to:1,cook:1,});
  });