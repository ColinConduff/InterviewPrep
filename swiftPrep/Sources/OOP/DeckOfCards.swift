
/**
	Implement a generic deck of playing cards.

	Not tested yet
 */

enum Suit: Int {
	case club = 0, diamond = 1, heart = 2, spade = 3
}

protocol Card {
	var faceValue: Int { get }
	var suit: Suit { get }
	var available: Bool { get set }
}

struct CardFactory: Card {

	internal var available: Bool
	internal let faceValue: Int
	internal let suit: Suit

	init(int faceValue, Suit suit) {
		self.available = true
		self.faceValue = faceValue
		self.suit = suit
	}
}

protocol Hand {
	var cards: [Card] { get }
	func score() -> Int 
	func add(card: Card)
}

struct HandFactory<Card>: Hand {
	internal var cards = [Card]()

	init(cards: [Card]) { self.cards = cards }

	func score() -> Int {
		// Calculate the sum of the face values of the cards
		return cards.reduce(0) { $0 + $1.faceValue }
	}

	mutating func add(card: Card) {
		cards.append(card)
	}
}

class Deck<Card>: DeckProtocol {
	private var cardQueue: ArraySlice<Card>

	init() {
		self.cards = [Card]()
	}

	func shuffle() {
		var cards = Array(cardQueue)

		// Fisher-Yates Shuffle 
		// Adapted from: http://stackoverflow.com/questions/24026510/how-do-i-shuffle-an-array-in-swift/24029847#24029847
        guard cards.count > 1 else { return }

        let zipped = zip(cards.indices, stride(from: cards.count, to: 1, by: -1))

        for (firstUnshuffled , unshuffledCount) in zipped {
            let d: IndexDistance = numericCast(arc4random_uniform(numericCast(unshuffledCount)))
            if d != 0 {
            	let i = cards.index(firstUnshuffled, offsetBy: d)
            	swap(&cards[firstUnshuffled], &cards[i])
            }
        }
        self.cardQueue = ArraySlice(cards)
	}

	func cardsRemaining() -> Int {
		return cards.count
	}

	func dealHand(ofSize size: Int) -> Hand {
		let cardsInHand = [Card]()
		for _ in 1...size {
			if let card = dealCard() { 
				cardsInHand.append(dealCard())
			} else {
				break
			}
		}
		return HandFactory(cards: cardsInHand)
	}

	func dealCard() -> Card? {
		return cards.popFirst()
	}
}