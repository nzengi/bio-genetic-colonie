const RobotColony = artifacts.require("RobotColony");

contract("RobotColony", (accounts) => {
  it("should authorize a robot", async () => {
    const instance = await RobotColony.deployed();
    await instance.authorizeRobot(accounts[1]);
    const robot = await instance.robots(accounts[1]);
    assert(robot.authorized === true, "Robot was not authorized");
  });

  it("should verify task performance and update reputation", async () => {
    const instance = await RobotColony.deployed();
    await instance.verifyTask(accounts[1], 100);
    const robot = await instance.robots(accounts[1]);
    assert(robot.reputation.toNumber() === 100, "Reputation was not updated correctly");
  });
});
