-- Insert into authors table
INSERT INTO authors (author_id, first_name, last_name) VALUES
    (1, 'Harper', 'Lee'),
    (2, 'Martha', 'Wells'),
    (3, 'Andy', 'Weir'),
    (4, 'Joanne', 'Greenberg'),
    (5, 'Rebecca', 'Skloot'),
    (6, 'Abraham', 'Verghese');

-- Insert into genres table
INSERT INTO genres (genre_id, genre_name) VALUES
    (1, 'Historical Fiction'),
    (2, 'Science Fiction'),
    (3, 'Fiction'),
    (4, 'Nonfiction'),
    (5, 'Classics');

-- Insert into medium table
-- INSERT INTO medium (medium_id, medium_name) VALUES
--     (1, 'Audiobook'),
--     (2, 'Ebook'),
--     (3, 'Physical');

-- Insert into books table
INSERT INTO books
    (title, author_id, read_status, isbn, description, image_url, external_url, medium_id, genre_id)
VALUES
    ('To Kill A Mockingbird', 1, 1, '9780061120084', 'The unforgettable novel of a childhood in a sleepy Southern town and the crisis of conscience that rocked it. "To Kill A Mockingbird" became both an instant bestseller and a critical success when it was first published in 1960. It went on to win the Pulitzer Prize in 1961 and was later made into an Academy Award-winning film, also a classic.

Compassionate, dramatic, and deeply moving, "To Kill A Mockingbird" takes readers to the roots of human behavior - to innocence and experience, kindness and cruelty, love and hatred, humor and pathos. Now with over 18 million copies in print and translated into forty languages, this regional story by a young Alabama woman claims universal appeal. Harper Lee always considered her book to be a simple love story. Today it is regarded as a masterpiece of American literature.',
    'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1553383690i/2657.jpg',
    'https://www.goodreads.com/book/show/2657.To_Kill_a_Mockingbird', 3, 5),

    ('System Collapse', 2, 1, '9781705041024', 'Am I making it worse? I think I''m making it worse.

Everyone''s favorite lethal SecUnit is back.

Following the events in Network Effect, the Barish-Estranza corporation has sent rescue ships to a newly-colonized planet in peril, as well as additional SecUnits. But if there’s an ethical corporation out there, Murderbot has yet to find it, and if Barish-Estranza can’t have the planet, they’re sure as hell not leaving without something. If that something just happens to be an entire colony of humans, well, a free workforce is a decent runner-up prize.

But there’s something wrong with Murderbot; it isn’t running within normal operational parameters. ART’s crew and the humans from Preservation are doing everything they can to protect the colonists, but with Barish-Estranza’s SecUnit-heavy persuasion teams, they’re going to have to hope Murderbot figures out what’s wrong with itself, and fast.

Yeah, this plan is... not going to work.',
    'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1691360414i/180290778.jpg',
    'https://www.goodreads.com/book/show/180290778-system-collapse', 1, 2),

    ('Project Hail Mary', 3, 0, '978848037023', 'Ryland Grace is the sole survivor on a desperate, last-chance mission—and if he fails, humanity and the earth itself will perish.

Except that right now, he doesn’t know that. He can’t even remember his own name, let alone the nature of his assignment or how to complete it.

All he knows is that he’s been asleep for a very, very long time. And he’s just been awakened to find himself millions of miles from home, with nothing but two corpses for company.

His crewmates dead, his memories fuzzily returning, Ryland realizes that an impossible task now confronts him. Hurtling through space on this tiny ship, it’s up to him to puzzle out an impossible scientific mystery—and conquer an extinction-level threat to our species.

And with the clock ticking down and the nearest human being light-years away, he’s got to do it all alone.

Or does he?',
    'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1606377782i/56049167.jpg',
    'https://www.goodreads.com/book/show/56049167-project-hail-mary', 1, 2),

    ('I Never Promised You a Rose Garden', 4, 1, '0312943598', 'The classic novel about a young woman''s struggle against madness, with a new afterword by the author

Hailed by The New York Times as "convincing and emotionally gripping" upon its publication in 1964, Joanne Greenberg''s semi-autobiographical novel stands as a timeless and unforgettable portrayal of mental illness. Enveloped in the dark inner kingdom of her schizophrenia, sixteen-year-old Deborah is haunted by private tormentors that isolate her from the outside world. With the reluctant and fearful consent of her parents, she enters a mental hospital where she will spend the next three years battling to regain her sanity with the help of a gifted psychiatrist. As Deborah struggles toward the possibility of the "normal" life she and her family hope for, the reader is inexorably drawn into her private suffering and deep determination to confront her demons.

A modern classic, I Never Promised You a Rose Garden remains every bit as poignant, gripping, and relevant today as when it was first published.',
    'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1328326176i/6586393.jpg',
    'https://www.goodreads.com/book/show/6586393-i-never-promised-you-a-rose-garden', 2, 3),

    ('The Immortal Life of Henrietta Lacks', 5, 1, '9781400052172', 'Her name was Henrietta Lacks, but scientists know her as HeLa. She was a poor Southern tobacco farmer who worked the same land as her enslaved ancestors, yet her cells—taken without her knowledge—became one of the most important tools in medicine. The first “immortal” human cells grown in culture, they are still alive today, though she has been dead for more than sixty years. If you could pile all HeLa cells ever grown onto a scale, they’d weigh more than 50 million metric tons—as much as a hundred Empire State Buildings. HeLa cells were vital for developing the polio vaccine; uncovered secrets of cancer, viruses, and the atom bomb’s effects; helped lead to important advances like in vitro fertilization, cloning, and gene mapping; and have been bought and sold by the billions.

Yet Henrietta Lacks remains virtually unknown, buried in an unmarked grave.

Now Rebecca Skloot takes us on an extraordinary journey, from the “colored” ward of Johns Hopkins Hospital in the 1950s to stark white laboratories with freezers full of HeLa cells; from Henrietta’s small, dying hometown of Clover, Virginia — a land of wooden quarters for enslaved people, faith healings, and voodoo — to East Baltimore today, where her children and grandchildren live and struggle with the legacy of her cells.

Henrietta’s family did not learn of her “immortality” until more than twenty years after her death, when scientists investigating HeLa began using her husband and children in research without informed consent. And though the cells had launched a multimillion-dollar industry that sells human biological materials, her family never saw any of the profits. As Rebecca Skloot so brilliantly shows, the story of the Lacks family — past and present — is inextricably connected to the history of experimentation on African Americans, the birth of bioethics, and the legal battles over whether we control the stuff we are made of.

Over the decade it took to uncover this story, Rebecca became enmeshed in the lives of the Lacks family—especially Henrietta’s daughter Deborah, who was devastated to learn about her mother’s cells. She was consumed with questions: Had scientists cloned her mother? Did it hurt her when researchers infected her cells with viruses and shot them into space? What happened to her sister, Elsie, who died in a mental institution at the age of fifteen? And if her mother was so important to medicine, why couldn’t her children afford health insurance?

Intimate in feeling, astonishing in scope, and impossible to put down, The Immortal Life of Henrietta Lacks captures the beauty and drama of scientific discovery, as well as its human consequences.',
    'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1327878144i/6493208.jpg',
    'https://www.goodreads.com/book/show/6493208-the-immortal-life-of-henrietta-lacks', 3, 4),

    ('The Covenant of Water', 6, 0, '9780802162182', 'The Covenant of Water is the long-awaited new novel by Abraham Verghese, the author of Cutting for Stone. Published in 2009, Cutting for Stone became a literary phenomenon, selling over 1.5 million copies in the United States alone and remaining on the New York Times bestseller list for over two years.

Spanning the years 1900 to 1977, The Covenant of Water is set in Kerala, on South India’s Malabar Coast, and follows three generations of a family that suffers a peculiar affliction: in every generation, at least one person dies by drowning—and in Kerala, water is everywhere. The family is part of a Christian community that traces itself to the time of the apostles, but times are shifting, and the matriarch of this family, known as Big Ammachi—literally “Big Mother”—will witness unthinkable changes at home and at large over the span of her extraordinary life. All of Verghese’s great gifts are on display in this new work: there are astonishing scenes of medical ingenuity, fantastic moments of humor, a surprising and deeply moving story, and characters imbued with the essence of life.

A shimmering evocation of a lost India and of the passage of time itself, The Covenant of Water is a hymn to progress in medicine and to human understanding, and a humbling testament to the hardships undergone by past generations for the sake of those alive today. It is one of the most masterful literary novels published in recent years.',
    'https://images-na.ssl-images-amazon.com/images/S/compressed.photo.goodreads.com/books/1683443725i/150083090.jpg',
    'https://www.goodreads.com/book/show/150083090-the-covenant-of-water', 2, 5);
