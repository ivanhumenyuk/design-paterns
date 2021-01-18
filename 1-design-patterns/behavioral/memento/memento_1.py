# Memento class
class Migration:
    def __init__(self, name, info):
        self.name = name
        self.info = info


# Caretaker class
class VersionControl:
    def __init__(self):
        self.__commit_history = []

    def push(self, commit: Migration):
        self.__commit_history.append(commit)
        return 'Commit has already added\n'

    def delete(self, commit: Migration):
        self.__commit_history.pop(self.__commit_history.index(commit))

    def get_history(self):
        return self.__commit_history

    def get_commit(self, index):
        return self.__commit_history[index]


class CommitCreator:
    def __init__(self, name):
        self._name = name

    def revert(self, commit: Migration):
        self._name = commit.name
        return f'Revert to {commit.name} : {commit.info}.\n'

    def save(self, info) -> Migration:
        return Migration(self._name, info)


if __name__ =='__main__':
    version_control = VersionControl()
    creator1 = CommitCreator('New commit 1')
    creator2 = CommitCreator('Newer commit 2')

    print(version_control.push(creator1.save('Commit about new code')))
    print(version_control.push(creator2.save('Commmit about 2 new lines of elegant code')))

    print(creator1.revert(version_control.get_commit(1)))






