# Observer
Define a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.

## Structure
![image](../../images/observer/structure.png)

#### Subject
- Knows its observers. Any number of Observer objects may observe a subject.
- Provides an interface for attaching and detaching Observer objects.
#### Observer
- Defines an updating interface for objects that should be notified of changes in a subject.
#### ConcreteSubject
- Stores state of interest to ConcreteObserver objects.
- Sends a notification to its observers when its state changes.
#### ConcreteObserver
- Maintains a reference to a ConcreteSubject object.
- Stores state that should stay consistent with the subject's.
- Implements the Observer updating interface to keep its state consistent with the subject's.

## Flow
![image](../../images/observer/structure.png)
- ConcreteSubject notifies its observers whenever a change occurs that could make its observers' state inconsistent with its own.
- After being informed of a change in the concrete subject, a ConcreteObserver object may query the subject for information ConcreteObserver uses this information to reconcile its state with that of the subject. 
- The Observer object that initiates the change request postpones its update until it gets a notification from the subject. Notify is not always called by the subject. It can be called by an observer or by another kind of object entirely. 

## Example
Link: [Weather-O-Rama](./problem.md)

## Applicability
- When an abstraction has two aspects, one dependent on the other. Encapsulating these aspects in separate objects lets you vary and reuse them independently.
- When a change to one object requires changing others, and you don't know how many objects need to be changed.
- When an object should be able to notify other objects without making assumptions about who these objects are. In other words, you don't want these objects tightly coupled.

## Advantages vs Disavantages
1. <b>Abstract coupling between Subject and Observer</b>: All a subject knows is that it has a list of observers, each conforming to the simple interface of the abstract Observer class. The subject doesn't know the concrete class of any observer. Thus the coupling between subjects and observers is abstract and minimal. Because Subject and Observer aren't tightly coupled, they can belong to
different layers of abstraction in a system. A lower-level subject can communicate and inform a higher-level observer, thereby keeping the system's layering intact. If Subject and Observer are lumped together, then the resulting object must either span two layers (and violate the layering), or it must be forced to live in one layer or the other (which might compromise the layering
abstraction).
2. <b>Support for broadcast communication</b>: Unlike an ordinary request, the notification that a subject sends needn't specify its receiver. The notification is broadcast automatically to all interested objects that subscribed to it. The subject doesn't care how many interested objects exist; its only responsibility is to notify its observers. This gives you the freedom to add and remove
observers at any time. It's up to the observer to handle or ignore a notification. 
3. <b>Unexpected updates</b>. Because observers have no knowledge of each other's presence, they can be blind to the ultimate cost of changing the subject. A seemingly innocuous operation on the subject may cause a cascade of updates to observers and their dependent objects. Moreover, dependency criteria that aren't well-defined or maintained usually lead to spurious updates, which can be hard to track down. This problem is aggravated by the fact that the simple update protocol provides no details on what changed in the subject. Without additional protocol to help observers discover what changed, they may be forced to work hard to deduce the changes.
