# Pylaunch

## Domain Views

---

### User Stories

As a User I want to edit python scripts to modify my source code and be able to program.
As a User I want to execute my python scripts to automate and interact with other programs and simplify everyday tasks.
As a User I want to store (disk) / download (cloud) my scripts to have them available at all times.
As a User, I would like to update the program to stay up to date and get the latest features.

---

```mermaid
graph LR
	script{Script}
	user -- triggers --> syntaxCheck -- in --> editor
	user -- checks --> errorModal -- in --> editor
	user -- navigates using --> toolbar -- to --> page{Page}
	subgraph User
        user -- stores --> s1{script}
        user -- loads --> script
        user -- runs --> s2{script} -- shows result --> window -- to --> user
        user -- creates new --> script
        user -- edits --> s3{script} -- in --> editor{Editor}
	    user -- edits --> configfile
        user -- stores --> configfile{Configfile}
	end
```

```mermaid
graph LR
	subgraph App
        app2(app) -- holds --> list -- of --> script{Script}
        configfile{Configfile} -- setups --> app1(app)
        script -- stores to --> disk & cloud
	end
```

```mermaid
graph LR
    subgraph Script
        script -- executes --> sourcecode
    end
```

```mermaid
graph LR
	subgraph Editor
		syntaxCheck(syntax check) -- validates --> script{Script}
		errorModal(error modal) -- shows fails of --> script
		runner -- executes --> script
	end
```

```mermaid
graph LR
	subgraph Frame
		app -- includes --> frame -- includes --> p1
	end
	subgraph Page
		p1(page) -- includes --> fragment/s -- hold --> component/s
	end
```

```mermaid
graph LR
	subgraph Configfile
		format -- uses --> json
	end
```



## Technical Views

````mermaid
graph TD
	bf --> bb --> bf
	eb --- ef
	state -- used by --> components
	components -- store global data into --> state
	
	subgraph Frontend
		ef("eel")
		bf("bridge")
		components
	end

	subgraph Backend
		eb("eel")
		bb("bridge")
	end
	
	subgraph Store
		state
	end
````

#### Script Provider current state

```mermaid
graph TB
	subgraph Dependent
        GenericProvider
        parser(Parser)
		ProviderFactory
	end
	parser --> ProviderFactory
	ProviderFactory --- Config --- ScriptProvider
	ProviderFactory -- instantiates --> ScriptProvider
	ProviderFactory -- creates --> GenericProvider
	GenericProvider -- passed to --> parser
	GenericProvider -- implements --> ScriptProvider
	
```

## Project Assets

#### Links

https://coolors.co/1500ff-007bff-00eeff-00ffcb-00ff5d