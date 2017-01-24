import PackageDescription

let package = Package(
    name: "InterviewPrep",
    targets: [
    	Target(name: "SwiftBridge", dependencies:["CModule"])
    ]
)