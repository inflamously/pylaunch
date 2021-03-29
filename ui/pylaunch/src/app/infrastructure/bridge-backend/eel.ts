export module eel {
  export function exec(name: string, ...args: any[]): Promise<any> {
    return new Promise((resolve, reject) => {
      const targetFunction =  name ? window["eel"][name] : undefined
      if (targetFunction) {
        const resolver = (v) => resolve(v);
        if (args.length > 0) {
          console.log(this);
          targetFunction.apply(this, args)(resolver);
        } else {
          targetFunction()(resolver);
        }
      } else {
        reject(new Error(`function called ${name} not found`));
      }
    });
  }
}
