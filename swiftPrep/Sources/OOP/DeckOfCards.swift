
/**
	Implement a generic deck of playing cards.

	Not tested yet
 */

import Darwin

enum Suit: Int {
	case club = 0, diamond = 1, heart = 2, spade = 3
}

struct Card {

	var available: Bool
	let faceValue: Int
	let suit: Suit

	init(faceValue: Int, suit: Suit) {
		self.available = true
		self.faceValue = faceValue
		self.suit = suit
	}
}

// Restrict how a hand can be used
protocol Hand {
	var cards: [Card] { get }
	func score() -> Int 
	mutating func add(card: Card)
}

/**
 Creates a hand and defines its behavior.

 "cards" must be mutable to allow adding to it,
 however other mutating operations should be prevented,
 so other classes should make a hand with HandMaker
 and then treat the instance as a hand
 */
struct HandMaker: Hand {
	var cards = [Card]()

	init(cards: [Card]) { self.cards = cards }

	func score() -> Int {
		// Calculate the sum of the face values of the cards
		return cards.reduce(0) { $0 + $1.faceValue }
	}

	mutating func add(card: Card) {
		cards.append(card)
	}
}

class Deck {
	private var cardQueue: ArraySlice<Card>

	init() {
		self.cardQueue = ArraySlice<Card>()
	}

	func shuffle() {
		var cards = Array(cardQueue)

		// Fisher-Yates Shuffle 
		// Adapted from: http://stackoverflow.com/questions/24026510/how-do-i-shuffle-an-array-in-swift/24029847#24029847
        guard cards.count > 1 else { return }

        let zipped = zip(cards.indices, stride(from: cards.count, to: 1, by: -1))

        for (firstUnshuffled , unshuffledCount) in zipped {
            let d = Int(arc4random_uniform(UInt32(unshuffledCount)))
            if d != 0 {
            	let i = cards.index(firstUnshuffled, offsetBy: d)
            	swap(&cards[firstUnshuffled], &cards[i])
            }
        }
        self.cardQueue = ArraySlice(cards)
	}

	func cardsRemaining() -> Int {
		return cardQueue.count
	}

	func dealHand(ofSize size: Int) -> Hand {
		var cardsInHand = [Card]()
		for _ in 1...size {
			if let card = dealCard() { 
				cardsInHand.append(card)
			} else {
				break
			}
		}
		return HandMaker(cards: cardsInHand)
	}

	func dealCard() -> Card? {
		return cardQueue.popFirst()
	}
}